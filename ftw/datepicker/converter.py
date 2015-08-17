from datetime import datetime
from ftw.datepicker import _
from ftw.datepicker.interfaces import IDateTimePickerWidget
from z3c.form import converter
from z3c.form.converter import FormatterValidationError
from zope.component import adapts
from zope.i18n import translate
from zope.schema.interfaces import IDate
from zope.schema.interfaces import IDatetime
from zope.component.hooks import getSite
from zope.component import getMultiAdapter

JS_DATE_FORMAT_MAPPER = {'d': '%d', 'm': '%m', 'Y': '%Y',
                         'H': '%H', 'i': '%M'}


def transform_js_format(js_format):
    # Datagrid may ship, more than one with the same id. example TT rows.
    if not js_format:
        js_format = "d.m.Y H:i"
    js_format = isinstance(js_format, list) and js_format[0] or js_format
    for old, new in JS_DATE_FORMAT_MAPPER.items():
        if new not in js_format:
            js_format = js_format.replace(old, new)
    return js_format


class BaseDateConverter(converter.BaseDataConverter):

    def __init__(self, field, widget):
        super(BaseDateConverter, self).__init__(field, widget)
        portal = getSite()
        portal_state = getMultiAdapter((portal, portal.REQUEST),
            name=u'plone_portal_state')
        current_language = portal_state.language()
        widget_format = self.widget.config.get(current_language)
        self.transformed_format = transform_js_format(widget_format)

    def toWidgetValue(self, value):
        if value is self.field.missing_value:
            return u''

        return value.strftime(self.transformed_format)

    def toFieldValue(self, value):
        if value == u'':
            return None

        try:
            return datetime.strptime(value, self.transformed_format)
        except ValueError, err:
            pass
        error = translate(_("error_datetime_parse", default=err.args[0]))
        raise FormatterValidationError(error, value)


class DateTimeDataConverter(BaseDateConverter):

    adapts(IDatetime, IDateTimePickerWidget)


class DateDataConverter(BaseDateConverter):

    def __init__(self, field, widget):
        super(DateDataConverter, self).__init__(field, widget)
        self.transformed_format = self.transformed_format.split(" ")[0]

    adapts(IDate, IDateTimePickerWidget)

    def toFieldValue(self, value):
        value = super(DateDataConverter, self).toFieldValue(value)
        if isinstance(value, datetime):
            return value.date()
        return
