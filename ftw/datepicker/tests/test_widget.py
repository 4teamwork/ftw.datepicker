from ftw.datepicker.tests import FunctionalTestCase
from ftw.testbrowser import browsing
from Products.CMFCore.utils import getToolByName
from ftw.testbrowser.pages import z3cform


class TestWidget(FunctionalTestCase):

    def setUp(self):
        super(TestWidget, self).setUp()
        self.grant('Manager')

    @browsing
    def test_fill_datetime_field_with_browser(self, browser):
        browser.login().visit(view='test-z3cform-task')
        browser.fill({u'Due Date': u'23.06.2015 10:00'}).submit()
        self.assertEquals({u'due_date': u'2015-06-23T10:00:00'}, browser.json)

    @browsing
    def test_fill_date_field_with_browser(self, browser):
        browser.login().visit(view='test-z3cform-task')
        browser.fill({u'Publish Date': u'24.06.2015'}).submit()
        self.assertEquals({u'publish_date': u'2015-06-24'}, browser.json)

    @browsing
    def test_do_not_allow_a_date_before_1900(self, browser):
        browser.login().visit(view='test-z3cform-task')
        browser.fill({u'Publish Date': u'31.12.1899'}).submit()

        errors = z3cform.erroneous_fields(browser.forms['form'])
        self.assertEquals(['Publish Date'], errors.keys())
        self.assertEquals(['Ein Datum vor 1900 ist nicht erlaubt.'],
                          errors.values()[0])
