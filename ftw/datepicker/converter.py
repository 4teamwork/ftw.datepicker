from z3c.form import converter
from zope.component import adapts
from zope.schema.interfaces import IDate
from ftw.datepicker.interfaces import IDatePickerWidget
from zope.i18n.format import DateTimeParseError
from z3c.form.converter import FormatterValidationError

class DateDataConverter(converter.BaseDataConverter):
    """A special data converter for calendar-related values."""

    adapts(IDate, IDatePickerWidget)
    
    type = None
    lengths = [u'long', u'medium', u'short']
    

    def __init__(self, field, widget):
        super(DateDataConverter, self).__init__(field, widget)
        locale = self.widget.request.locale
        self.formatters = [locale.dates.getFormatter(u'date', length) for length in self.lengths]
        
    def toWidgetValue(self, value):
        """See interfaces.IDataConverter"""
        if value is self.field.missing_value:
            return u''
        return self.formatters[0].format(value)

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        if value == u'':
            return self.field.missing_value
        # we try multiple parsers, the first one that can parse the date string wins
        for formatter in self.formatters:
            try:
                return formatter.parse(value)
            except DateTimeParseError, err:
                pass
        raise FormatterValidationError(err.args[0], value)