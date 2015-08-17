from ftw.builder.testing import BUILDER_LAYER
from ftw.builder.testing import functional_session_factory
from ftw.builder.testing import set_builder_session_factory
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from zope.configuration import xmlconfig
from Products.CMFCore.utils import getToolByName
import transaction


class FtwDatepickerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, BUILDER_LAYER)

    def setUpZope(self, app, configurationContext):
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="z3c.autoinclude" file="meta.zcml" />'
            '  <includePlugins package="plone" />'
            '  <includePluginsOverrides package="plone" />'
            '</configure>',
            context=configurationContext)

        import ftw.datepicker.tests.views
        xmlconfig.file('configure.zcml',
                       ftw.datepicker.tests.views,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        switch_language(portal, 'de')
        applyProfile(portal, 'plone.app.registry:default')
        applyProfile(portal, 'ftw.datepicker:default')


FTW_DATEPICKER_FIXTURE = FtwDatepickerLayer()

FTW_DATEPICKER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FTW_DATEPICKER_FIXTURE,
           set_builder_session_factory(functional_session_factory)),
    name="ftw.datepicker:functional")


def switch_language(portal, lang):
    language_tool = getToolByName(portal, 'portal_languages')
    language_tool.manage_setLanguageSettings(
        lang, ['de', 'fr', 'en'],
        setUseCombinedLanguageCodes=False, startNeutral=False)
    portal.setLanguage(lang)
    transaction.commit()
