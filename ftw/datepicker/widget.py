from z3c.form.browser import widget
from z3c.form.widget import FieldWidget
from z3c.form.widget import Widget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from zope.interface import implementsOnly
from zope.component import adapter
from zope.interface import implementer
from ftw.datepicker.interfaces import IDatePickerWidget
from Products.CMFCore.utils import getToolByName


class DatePickerWidget(widget.HTMLTextInputWidget, Widget):
    """ Datepicker widget. """
    implementsOnly(IDatePickerWidget)

    klass = u'datepicker-widget'
    size = 20

    def update(self):
        super(DatePickerWidget, self).update()
        widget.addFieldClass(self)
        self.portal_url = getToolByName(self.context, 'portal_url')

    def datepicker_javascript(self):
        return """/* <![CDATA[ */
            $(function() {
                $("#%(id)s").datepicker({
                    showOn: 'button',
                    buttonImage: '%(buttonImage)s',
                    buttonImageOnly: true,
                    dateFormat: 'd. MM yy',
                    changeMonth: true,
                    changeYear: true
                });
            });
            /* ]]> */""" % dict(id=self.id,
                    buttonImage='%s/popup_calendar.png' % self.portal_url())


@adapter(IDatePickerWidget, IFormLayer)
@implementer(IFieldWidget)
def DatePickerFieldWidget(field, request):
    """IFieldWidget factory for DatePickerFieldWidget."""
    return FieldWidget(field, DatePickerWidget(request))
