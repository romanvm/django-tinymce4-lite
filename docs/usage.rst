Usage
=====

HTMLField for Models
--------------------

For developers who want to implement TinyMCE editor in their Django applications in the simplest possible way,
**tinymce4-lite** provides a :class:`HTMLField<tinymce.HTMLField>` field for models.
This field can can be used instead of a :class:`TextField<django.db.models.TextField>`.
For example:

.. code-block:: python

    from django.db import models
    from tinymce import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField('Content')

Don't forget to apply `safe`_ filter to the HTML content in your templates to render it properly.
For example:

.. code-block:: django

  {{ my_model.content|safe }}

.. warning:: If you are using TinyMCE editor in publicly facing webpages, it is strongly recommended to define
  `valid_elements`_ option for TinyMCE to limit the set of allowed HTML elements and/or
  to filter submitted content for security reasons.

In Django Admin interface the widget is used automatically for all models that have
:class:`HTMLField<tinymce.HTMLField>` fields.

.. _forms-media:

If you are using TinyMCE 4 in your website forms,
you need to add ``form.media`` template variable to the ``<head>`` section of your templates:

.. code-block:: django

  <!DOCTYPE html>
  <html>
  <head>
    ...
    {{ form.media }}
  </head>
  <body>
  ...
  </body>
  </html>

.. _safe: https://docs.djangoproject.com/es/1.9/ref/templates/builtins/#safe
.. _valid_elements: https://www.tinymce.com/docs/configure/content-filtering/#valid_elements

TinyMCE Widget for Forms
------------------------

In custom forms you can use :class:`TinyMCE<tinymce.TinyMCE>` form widget to render TinyMCE editor
instead of a simple :class:`CharField<django.forms.CharField>`::

  from django import forms
  from tinymce import TinyMCE


  class MyForm(forms.Form):
      content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))

The :class:`TinyMCE<tinymce.TinyMCE>` class constructor takes 3 parameters:

- ``attrs`` -- general Django widget attributes.
- ``mce_attrs`` -- additional configuration parameters for TinyMCE 4.
  These parameters **amend** the existing configuration. For example, in the preceding code sample ``'width'``
  parameter sets TinyMCE widget width to 800 pixels without changing other configuration options.
- ``profile`` -- TinyMCE 4 configuration parameters. They **replace** the existing configuration.
  That is, you need to provide a fully defined TinyMCE configuration for ``profile`` parameter.

Also see the information about :ref:`form.media<forms-media>` template variable in the preceding subsection.
