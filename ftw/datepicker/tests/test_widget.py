from ftw.datepicker.tests import FunctionalTestCase
from ftw.testbrowser import browsing
from Products.CMFCore.utils import getToolByName


class TestWidget(FunctionalTestCase):

    def setUp(self):
        super(TestWidget, self).setUp()
        self.grant('Manager')

    def test_resources_are_installed(self):
        js_registry = getToolByName(self.portal, 'portal_javascripts')

        self.assertTrue(
            '++resource++datetimepicker/js/datetimepicker-2.4.5/'
            'jquery.datetimepicker.js'
            in js_registry.getResourceIds())

        self.assertTrue(
            '++resource++datetimepicker/js/datetimepicker_widget.js'
            in js_registry.getResourceIds())

        css_registry = getToolByName(self.portal, 'portal_css')

        self.assertTrue(
            '++resource++datetimepicker/js/datetimepicker-2.4.5/'
            'jquery.datetimepicker.css'
            in css_registry.getResourceIds())

    @browsing
    def test_fill_field_with_browser(self, browser):
        browser.login().visit(view='test-z3cform-task')
        browser.fill({u'Due Date': u'24.06.2015 10:00'})
        browser.find('Submit').click()
        self.assertEquals({u'due_date': u'2015-06-24T10:00:00'}, browser.json)
