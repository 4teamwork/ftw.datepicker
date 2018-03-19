from ftw.builder.testing import BUILDER_LAYER
from ftw.builder.testing import functional_session_factory
from ftw.builder.testing import set_builder_session_factory
from pkg_resources import get_distribution
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from zope.configuration import xmlconfig
from Products.CMFCore.utils import getToolByName
import transaction


IS_PLONE_5 = get_distribution('Plone').version >= '5'

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
        if IS_PLONE_5:
            applyProfile(portal, 'plone.app.contenttypes:default')


FTW_DATEPICKER_FIXTURE = FtwDatepickerLayer()

FTW_DATEPICKER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FTW_DATEPICKER_FIXTURE,
           set_builder_session_factory(functional_session_factory)),
    name="ftw.datepicker:functional")


def switch_language(portal, lang):
    language_tool = getToolByName(portal, 'portal_languages')
    if IS_PLONE_5:
        language_tool.addSupportedLanguage("de")
        language_tool.addSupportedLanguage("fr")
        language_tool.addSupportedLanguage("fr-ch")
        language_tool.settings.use_combined_language_codes = True
        language_tool.setDefaultLanguage(lang)
    else:
        language_tool.manage_setLanguageSettings(
            lang, ['de', 'fr', 'en', 'fr-ch'],
            setUseCombinedLanguageCodes=True, startNeutral=False)
    portal.setLanguage(lang)
    transaction.commit()
