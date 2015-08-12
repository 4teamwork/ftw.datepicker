from datetime import date
from datetime import datetime
from ftw.datepicker.widget import DateTimePickerWidgetFactory
from plone.z3cform.layout import FormWrapper
from z3c.form.button import buttonAndHandler
from z3c.form.field import Fields
from z3c.form.form import Form
from zope import schema
from zope.interface import Interface
import json


class ITaskFormSchema(Interface):
    due_date = schema.Datetime(
        title=u'Due Date',
        required=False,
    )
    publish_date = schema.Date(
        title=u'Publish Date',
        required=False)

class TaskForm(Form):
    label = u'Shopping'
    ignoreContext = True
    fields = Fields(ITaskFormSchema)

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.result_data = None

    def update(self):
        self.fields['due_date'].widgetFactory = DateTimePickerWidgetFactory
        self.fields['publish_date'].widgetFactory = DateTimePickerWidgetFactory
        return super(TaskForm, self).update()

    @buttonAndHandler(u'Submit')
    def handle_submit(self, action):
        data, errors = self.extractData()
        if len(errors) > 0:
            return

        self.result_data = {}
        for key, value in data.items():
            if not value:
                continue

            if isinstance(value, (datetime, date)):
                value = value.isoformat()

            self.result_data[key] = value


class TaskView(FormWrapper):
    form = TaskForm

    def render(self):
        if self.form_instance.result_data:
            self.request.RESPONSE.setHeader('Content-Type', 'application/json')
            return json.dumps(self.form_instance.result_data)
        else:
            return super(TaskView, self).render()
