from ftw.datepicker import _
from ftw.datepicker.interfaces import IDatePickerWidget
from z3c.form import converter
from z3c.form.converter import FormatterValidationError
from zope.component import adapts
from zope.i18n import translate
from zope.i18n.format import DateTimeFormat
from zope.i18n.format import DateTimeParseError
from zope.schema.interfaces import IDate


ADDITIONAL_PATTERNS = {
    'fr': [u'd. MMMM yyyy', ],
    'de': [u'd.M.yyyy', u'd.M.yy']}


class DateDataConverter(converter.BaseDataConverter):
    """A special data converter for calendar-related values."""

    adapts(IDate, IDatePickerWidget)

    lengths = [u'long', u'medium', u'short']

    def __init__(self, field, widget):
        super(DateDataConverter, self).__init__(field, widget)
        locale = self.widget.request.locale
        self.formatters = [locale.dates.getFormatter(u'date', length) for length in self.lengths]

        for pattern in ADDITIONAL_PATTERNS.get(locale.id.language, []):
            self.formatters.append(DateTimeFormat(
                    pattern=pattern,
                    calendar=locale.dates.calendars.get('gregorian')))

    def toWidgetValue(self, value):
        """See interfaces.IDataConverter"""
        if value is self.field.missing_value:
            return u''
        return self.formatters[0].format(value)

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        if value == u'':
            return self.field.missing_value

        value = ' '.join([word.lower().capitalize()
                           for word in value.split(' ')])
        value_lowercase = value.lower()

        # we try multiple parsers, the first one that can parse the
        # date string wins
        for formatter in self.formatters:

            # for german the month name has to be uppercase ..
            try:
                return formatter.parse(value)
            except DateTimeParseError, err:
                pass

            # .. but for french it has to be lowercase
            try:
                return formatter.parse(value_lowercase)
            except DateTimeParseError, err:
                pass

        error = translate(_("error_datetime_parse", default=err.args[0]))
        raise FormatterValidationError(error, value)
