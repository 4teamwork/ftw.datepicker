from datetime import datetime
from ftw.datepicker.converter import DateTimeDataConverter, transform_js_format
from ftw.datepicker.tests import FunctionalTestCase
from ftw.datepicker.widget import DateTimePickerWidget
from z3c.form.converter import FormatterValidationError
from z3c.form.testing import TestRequest
from zope import schema


class TestDatetimeConverter(FunctionalTestCase):

    def setUp(self):
        super(TestDatetimeConverter, self).setUp()
        request = TestRequest()

        datetime_field = schema.Datetime()

        widget = DateTimePickerWidget(request)
        widget.form = schema.Field()
        self.converter = DateTimeDataConverter(datetime_field, widget)

    def test_toWidgetValue_with_german_js_format_by_default(self):
        value = self.converter.toWidgetValue(datetime(2015, 6, 24, 10, 0))
        self.assertEquals('24.06.2015 10:00', value)

    def test_toFieldValue_with_german_js_format_by_default(self):
        value = self.converter.toFieldValue('24.06.2015 10:00')
        self.assertEquals(datetime(2015, 6, 24, 10, 0), value)

    def test_toFieldValue_with_german_js_format_without_time(self):
        widget_format = 'd.m.Y'
        self.converter.transformed_format = transform_js_format(widget_format)
        value = self.converter.toFieldValue('24.06.2015')
        self.assertEquals(datetime(2015, 6, 24, 0, 0), value)

    def test_toFieldValue_is_none_if_empty_string(self):
        value = self.converter.toFieldValue(u'')
        self.assertIsNone(value, 'Expect none if data is empty string.')

    def test_toFieldValue_raises_formatter_error_if_data_are_invalid(self):
        """
        The widget expects the time by default. This test makes sure the
        widget renders an error if no time is provided.
        """
        with self.assertRaises(FormatterValidationError):
            self.converter.toFieldValue(u'24.06.2015')

    def test_toFieldValue_custom_config(self):
        widget_format = 'Y-m-d'
        self.converter.transformed_format = transform_js_format(widget_format)

        with self.assertRaises(FormatterValidationError):
            self.converter.toFieldValue(u'24.06.2015')

        value = self.converter.toFieldValue(u'2015-06-24')
        self.assertEquals(datetime(2015, 6, 24, 0, 0), value)
