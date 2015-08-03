from datetime import datetime
from ftw.datepicker import _
from ftw.datepicker.interfaces import IDateTimePickerWidget
from z3c.form import converter
from z3c.form.converter import FormatterValidationError
from zope.component import adapts
from zope.i18n import translate
from zope.schema.interfaces import IDatetime

JS_DATE_FORMAT_MAPPER = {'d': '%d', 'm': '%m', 'Y': '%Y',
                         'H': '%H', 'i': '%M'}


def transform_js_format(js_format):
    # Datagrid may ship, more than one with the same id. example TT rows.
    js_format = isinstance(js_format, list) and js_format[0] or js_format
    for old, new in JS_DATE_FORMAT_MAPPER.items():
        if new not in js_format:
            js_format = js_format.replace(old, new)
    return js_format


class DateTimeDataConverter(converter.BaseDataConverter):

    adapts(IDatetime, IDateTimePickerWidget)

    def __init__(self, field, widget):
        super(DateTimeDataConverter, self).__init__(field, widget)

        widget_format = self.widget.config.get('format')

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
