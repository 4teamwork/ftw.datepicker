from ftw.datepicker.tests import FunctionalTestCase
from ftw.datepicker.testing import switch_language
from ftw.testbrowser import browsing


class TestWidget(FunctionalTestCase):

    def setUp(self):
        super(TestWidget, self).setUp()
        self.grant('Manager')
        switch_language(self.layer['portal'], 'fr')

    @browsing
    def test_fill_field_with_browser_datetime_french(self, browser):
        browser.login().visit(view='test-z3cform-task')
        browser.fill({u'Due Date': u'24/06/2015 08:15'})
        browser.find('Submit').click()
        self.assertEquals({u'due_date': u'2015-06-24T08:15:00'}, browser.json)

    @browsing
    def test_fill_field_with_browser_date_french(self, browser):
        browser.login().visit(view='test-z3cform-task')
        browser.fill({u'Publish Date': u'24/06/2015'})
        browser.find('Submit').click()
        self.assertEquals({u'publish_date': u'2015-06-24'}, browser.json)

    @browsing
    def test_fill_field_with_browser_date_unknown(self, browser):
        switch_language(self.layer['portal'], 'en')
        browser.login().visit(view='test-z3cform-task')
        browser.fill({u'Publish Date': u'24.06.2015'})
        browser.find('Submit').click()
        self.assertEquals({u'publish_date': u'2015-06-24'}, browser.json)
