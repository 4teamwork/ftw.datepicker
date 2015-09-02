ftw.datepicker
==============

`ftw.datepicker` provides a date/time picker widget for your `z3c.form`
fields using the jQuery based `DateTimePicker` widget from XDSoft
(http://xdsoft.net/jqplugins/datetimepicker/).


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


WARNING
-------

The datetime fields are not timezone aware!
To implement it, please see how to do it at:

https://github.com/plone/plone.app.event/blob/master/plone/app/event/dx/behaviors.py


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


Development
-----------

The jQuery plugin can be downloaded and extracted into its own folder inside
`ftw/datepicker/resources/js`. Only the files defined in the profile's
CSS and JS registry will be used.


Compatibility
-------------

Plone 4.3.x

.. image:: https://jenkins.4teamwork.ch/job/ftw.datepicker-master-test-plone-4.3.x.cfg/badge/icon
   :target: https://jenkins.4teamwork.ch/job/ftw.datepicker-master-test-plone-4.3.x.cfg

Plone 4.2.x

.. image:: https://jenkins.4teamwork.ch/job/ftw.datepicker-master-test-plone-4.2.x.cfg/badge/icon
   :target: https://jenkins.4teamwork.ch/job/ftw.datepicker-master-test-plone-4.2.x.cfg

Plone 4.1.x

.. image:: https://jenkins.4teamwork.ch/job/ftw.datepicker-master-test-plone-4.1.x.cfg/badge/icon
   :target: https://jenkins.4teamwork.ch/job/ftw.datepicker-master-test-plone-4.1.x.cfg


Links
-----

- Github: https://github.com/4teamwork/ftw.datepicker
- Issues: https://github.com/4teamwork/ftw.datepicker/issues
- Continuous integration: https://jenkins.4teamwork.ch/search?q=ftw.datepicker


Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.datepicker`` is licensed under GNU General Public License, version 2.
