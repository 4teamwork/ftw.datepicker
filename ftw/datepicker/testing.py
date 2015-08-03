from ftw.builder.testing import BUILDER_LAYER
from ftw.builder.testing import functional_session_factory
from ftw.builder.testing import set_builder_session_factory
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from zope.configuration import xmlconfig


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
        applyProfile(portal, 'ftw.datepicker:default')

FTW_DATEPICKER_FIXTURE = FtwDatepickerLayer()

FTW_DATEPICKER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FTW_DATEPICKER_FIXTURE,
           set_builder_session_factory(functional_session_factory)),
    name="ftw.datepicker:functional")
