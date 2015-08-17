from ftw.datepicker.interfaces import IDateTimePickerWidget
from z3c.form.browser import widget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from z3c.form.widget import Widget
from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementsOnly
import json
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from ftw.datepicker.interfaces import IDatetimeRegistry


class DateTimePickerWidget(widget.HTMLTextInputWidget, Widget):
    """ Datepicker widget. """
    implementsOnly(IDateTimePickerWidget)

    klass = u'datetimepicker-widget'
    config = None

    def __init__(self, request, config=None):
        super(DateTimePickerWidget, self).__init__(request)

        self.config = config
        if callable(config):
            self.config = config()
        elif not config:
            registry = getUtility(IRegistry)
            datesettings = registry.forInterface(IDatetimeRegistry)
            self.config = datesettings.formats
        self.validate_config()

    def update(self):
        super(DateTimePickerWidget, self).update()
        widget.addFieldClass(self)

    def datetimepicker_config(self):
        return json.dumps(self.config)

    def validate_config(self):
        try:
            json.dumps(self.config)
        except:
            raise (ValueError, 'The widget config is not a valid JSON object.')


DatePickerWidget = DateTimePickerWidget


@adapter(IDateTimePickerWidget, IFormLayer)
@implementer(IFieldWidget)
def DateTimePickerWidgetFactory(field, request, config=None):
    """IFieldWidget factory for DateTimePickerWidget."""
    return FieldWidget(field, DateTimePickerWidget(request, config))

DatePickerFieldWidget = DateTimePickerWidgetFactory
