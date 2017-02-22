from ftw.datepicker.testing import switch_language
from ftw.datepicker.tests import FunctionalTestCase
from ftw.testbrowser import browsing
import json


class TestWidget(FunctionalTestCase):

    def setUp(self):
        super(TestWidget, self).setUp()
        self.grant('Manager')
        switch_language(self.layer['portal'], 'fr')

    @browsing
    def test_config_formats(self, browser):
        browser.login().visit(self.portal, view='test-z3cform-task')
        due_date = browser.css('#form-widgets-due_date').first
        widgetdata = json.loads(due_date.attrib['data-datetimewidget'])
        self.assertIn('formats', widgetdata)
        self.assertEquals({"fr": "d/m/Y H:i", "de": "d.m.Y H:i"},
                          widgetdata['formats'])

    @browsing
    def test_config_firstday(self, browser):
        browser.login().visit(self.portal, view='test-z3cform-task')
        due_date = browser.css('#form-widgets-due_date').first
        widgetdata = json.loads(due_date.attrib['data-datetimewidget'])
        self.assertIn('dayOfWeekStart', widgetdata)
        self.assertEquals(1, widgetdata['dayOfWeekStart'])

    @browsing
    def test_config_weekend(self, browser):
        browser.login().visit(self.portal, view='test-z3cform-task')
        due_date = browser.css('#form-widgets-due_date').first
        widgetdata = json.loads(due_date.attrib['data-datetimewidget'])
        self.assertIn('disabledWeekDays', widgetdata)
        self.assertEquals([5, 6], widgetdata['disabledWeekDays'])
