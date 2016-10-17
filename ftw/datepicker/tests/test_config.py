from ftw.datepicker.tests import FunctionalTestCase
from ftw.datepicker.testing import switch_language
from ftw.testbrowser import browsing


class TestWidget(FunctionalTestCase):

    def setUp(self):
        super(TestWidget, self).setUp()
        self.grant('Manager')
        switch_language(self.layer['portal'], 'fr')

    @browsing
    def test_config_formats(self, browser):
        browser.login().visit(self.portal, view='test-z3cform-task')
        due_date = browser.css('#form-widgets-due_date')
        self.assertIn('"formats": {"fr": "d/m/Y H:i", "de": "d.m.Y H:i"}}',
                      due_date[0].outerHTML)

    @browsing
    def test_config_firstday(self, browser):
        browser.login().visit(self.portal, view='test-z3cform-task')
        due_date = browser.css('#form-widgets-due_date')
        self.assertIn('"dayOfWeekStart": 1', due_date[0].outerHTML)

    @browsing
    def test_config_weekend(self, browser):
        browser.login().visit(self.portal, view='test-z3cform-task')
        due_date = browser.css('#form-widgets-due_date')
        self.assertIn('"disabledWeekDays": [5, 6]', due_date[0].outerHTML)
