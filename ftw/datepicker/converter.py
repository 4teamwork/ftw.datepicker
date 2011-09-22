from z3c.form import converter
from zope.component import adapts
from zope.schema.interfaces import IDate
from ftw.datepicker.interfaces import IDatePickerWidget
from zope.i18n.format import DateTimeParseError
from zope.i18n.format import DateTimeFormat
from zope.i18n import translate
from z3c.form.converter import FormatterValidationError
from ftw.datepicker import _
class DateDataConverter(converter.BaseDataConverter):
    """A special data converter for calendar-related values."""

    adapts(IDate, IDatePickerWidget)

    lengths = [u'long', u'medium', u'short']


    def __init__(self, field, widget):
        super(DateDataConverter, self).__init__(field, widget)
        locale = self.widget.request.locale
        self.formatters = [locale.dates.getFormatter(u'date', length) for length in self.lengths]
        # a formatter that can parse single digit days and month
        self.formatters.append(DateTimeFormat(pattern='d.M.yyyy', calendar='gregorian'))
        self.formatters.append(DateTimeFormat(pattern='d.M.yy', calendar='gregorian'))

    def toWidgetValue(self, value):
        """See interfaces.IDataConverter"""
        if value is self.field.missing_value:
            return u''
        return self.formatters[0].format(value)

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        value =  ' '.join([word.capitalize() for word in value.split(' ')])
        if value == u'':
            return self.field.missing_value
        # we try multiple parsers, the first one that can parse the date string wins
        for formatter in self.formatters:
            try:
                return formatter.parse(value)
            except DateTimeParseError, err:
                pass

        error = translate(_("error_datetime_parse", default=err.args[0]))
        raise FormatterValidationError(error, value)
