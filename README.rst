ftw.datepicker
==============

`ftw.datepicker` provides a date/time picker widget for your `z3c.form`
fields using the jQuery based `DateTimePicker` widget from XDSoft
(http://xdsoft.net/jqplugins/datetimepicker/). It is compatible with
Plone 4.3 and 5.1.


Screenshot
----------

.. image:: https://github.com/4teamwork/ftw.datepicker/raw/master/docs/screenshot.png


Installation
------------

Add ftw.datepicker to your buildout configuration:

::

    [instance]
    eggs +=
        ...
        ftw.datepicker


Import the generic setup profile for `ftw.datepicker`.


Usage
-----

You can apply the widget to your field with the help of
`plone.directives.form`:

.. code:: python

    from plone.directives import form
    from plone.supermodel import model
    from ftw.datepicker.widget import DateTimePickerWidgetFactory

    class MySchema(model.Schema):
        form.widget(due_date=DateTimePickerWidgetFactory)
        due_date = schema.Datetime()

This renders a widget which allows to select the date and time.

You can pass a custom configuration of the widget like this:

.. code:: python

    from plone.directives import form
    from plone.supermodel import model
    from ftw.datepicker.widget import DateTimePickerWidgetFactory

    class MySchema(model.Schema):
        form.widget('due_date', DateTimePickerWidgetFactory, config=my_config)
        due_date = schema.Datetime()

`config` can either be a dict or a callable which produces a dict. The value
is then converted to a JSON object and passed to the template for the widget
to be picked up. Example: `{'format': 'd.m.Y', 'timepicker': False}`.

See http://xdsoft.net/jqplugins/datetimepicker/ for a full list of options.

You could apply the widget even to a `TextLine` field if you need to.


If you wish to use the Widget for a date field that needs a timezone, you can
tell it so by setting ``default_timezone`` to an Olson DB/pytz timezone
identifier or a callback (taking the context as an argument) returning such an
identifier:

.. code:: python

    from plone.directives import form
    from plone.supermodel import model
    from ftw.datepicker.widget import DateTimePickerWidgetFactory

    class MySchema(model.Schema):
        form.widget('due_date',
                    DateTimePickerWidgetFactory,
                    default_timezone='Europe/Berlin') # or in
        due_date = schema.Datetime()


In case you want to use this widget for an already defined field you can do
that too. In case of ``IEventBasic`` you must set the ``default_timezone`` due
to how ``plone.appe.event`` works.

.. code:: python

    from plone.autoform.interfaces import WIDGETS_KEY

    WIDGETS = {
        MySchema: {'start_date': DatePickerFieldWidget,
                   'end_date': DatePickerFieldWidget},
    }

    for schema, widget_config in WIDGETS.items():
        values = schema.queryTaggedValue(WIDGETS_KEY, {})
        values.update(widget_config)
        schema.setTaggedValue(WIDGETS_KEY, values)

    # Or with the default_timezone and/or config set:

    from plone.app.event.base import default_timezone
    from plone.app.event.dx.behaviors import IEventBasic
    from plone.autoform.interfaces import WIDGETS_KEY
    from plone.autoform.widgets import ParameterizedWidget

    WIDGETS = {
        IEventBasic: {'start': ParameterizedWidget(DatePickerFieldWidget,
                                                   default_timezone=default_timezone,
                                                   config=my_config),
                      'end': ParameterizedWidget(DatePickerFieldWidget,
                                                 default_timezone=default_timezone,
                                                 config=my_config)},
    }

    for schema, widget_config in WIDGETS.items():
        values = schema.queryTaggedValue(WIDGETS_KEY, {})
        values.update(widget_config)
        schema.setTaggedValue(WIDGETS_KEY, values)


Development
-----------

The jQuery plugin can be downloaded and extracted into its own folder inside
`ftw/datepicker/resources/js`. Only the files defined in the profile's
CSS and JS registry will be used.


Links
-----

- Github: https://github.com/4teamwork/ftw.datepicker
- Issues: https://github.com/4teamwork/ftw.datepicker/issues
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.datepicker


Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.datepicker`` is licensed under GNU General Public License, version 2.
