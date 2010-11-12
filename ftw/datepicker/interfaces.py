from z3c.form.interfaces import ITextWidget
from zope.interface import Interface


class IBrowserLayer(Interface):
    """ftw.datepicker browser layer
    """


class IDatePickerWidget(ITextWidget):
    """A datepicker widget.
    """
