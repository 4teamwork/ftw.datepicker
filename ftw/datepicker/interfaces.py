from z3c.form.interfaces import ITextWidget
from zope.interface import Interface
from plone.registry import field


class IBrowserLayer(Interface):
    """ftw.datepicker browser layer"""


class IDateTimePickerWidget(ITextWidget):
    """Marker interface for datetimepicker widget"""


class IDatetimeRegistry(Interface):
    formats = field.Dict(title=u"Formats",
        key_type=field.TextLine(title=u"Language"),
        value_type=field.TextLine(title=u"Dateformat"))
