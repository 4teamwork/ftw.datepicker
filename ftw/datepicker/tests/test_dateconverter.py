from datetime import date
from ftw.datepicker.converter import DateDataConverter
from ftw.datepicker.tests import FunctionalTestCase
from ftw.datepicker.widget import DateTimePickerWidget
from z3c.form.converter import FormatterValidationError
from z3c.form.testing import TestRequest
from zope import schema


class TestDateConverter(FunctionalTestCase):

    def setUp(self):
        super(TestDateConverter, self).setUp()
        request = TestRequest()

        datetime_field = schema.Date()

        widget = DateTimePickerWidget(request)
        widget.form = schema.Field()
        self.converter = DateDataConverter(datetime_field, widget)

    def test_toWidgetValue_with_german_js_format_by_default(self):
        value = self.converter.toWidgetValue(date(2015, 6, 24))
        self.assertEquals('24.06.2015', value)

    def test_toFieldValue_with_german_js_format_by_default(self):
        value = self.converter.toFieldValue('24.06.2015')
        self.assertEquals(date(2015, 6, 24), value)

    def test_toFieldValue_is_none_if_empty_string(self):
        value = self.converter.toFieldValue(u'')
        self.assertIsNone(value, 'Expect none if data is empty string.')

    def test_toFieldValue_raises_formatter_error_if_data_are_invalid(self):
        """
        The widget expects the time by default. This test makes sure the
        widget renders an error if no time is provided.
        """
        with self.assertRaises(FormatterValidationError):
            self.converter.toFieldValue(u'24.06.2015 08:15')

