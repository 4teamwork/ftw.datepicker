from ftw.upgrade import UpgradeStep
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from plone.registry.interfaces import IInterfaceAwareRecord
from zope.interface import noLongerProvides


class CleanupDatepickersRegistryEntries(UpgradeStep):
    """Cleanup datepickers registry entries.
    """

    record_names = [
        'ftw.datepicker.interfaces.IDatetimeRegistry.formats',
        'ftw.datepicker.interfaces.IDatetimeRegistry.various',
    ]

    def __call__(self):
        registry = getUtility(IRegistry)
        for record in [registry.records.get(name) for name in self.record_names]:
            noLongerProvides(record, IInterfaceAwareRecord)
            record.field.interfaceName = None
