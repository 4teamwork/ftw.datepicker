from ftw.datepicker import _
from z3c.form.interfaces import ITextWidget
from zope.interface import Interface
from plone.registry import field


class IBrowserLayer(Interface):
    """ftw.datepicker browser layer"""


class IDateTimePickerWidget(ITextWidget):
    """Marker interface for datetimepicker widget"""


class IDatetimeRegistry(Interface):
    formats = field.Dict(
        title=_(u'datetime_registry_title', default=u'Formats'),
        key_type=field.TextLine(
            title=_(u'datetime_registry_key_type', default=u'Language')
        ),
        value_type=field.TextLine(
            title=_(u'datetime_registry_value_type', default=u'Date format'),
        )
    )
