Usage
=====

HTMLField for Models
--------------------

For developers who want to implement TinyMCE editor in their Django applications as simply as possible,
**tinymce4-lite** provides a :class:`HTMLField<tinymce.HTMLField>` field for models.
This field can can be used instead of a :class:`TextField<django.db.models.TextField>`.
For example:

.. code-block:: python

    from django.db import models
    from tinymce import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField('Content')

.. _forms-media:

In Django Admin interface the widget is used automatically for all models that have
:class:`HTMLField<tinymce.HTMLField>` fields. If you are using TinyMCE 4 in your website forms,
you need to add ``form.media`` variable to the ``<head>`` section of your templates:

.. code-block:: html

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
- ``mce_attrs`` -- Additional configuration parameters for TinyMCE 4.
  These parameters **amend** the existing configuration. In the preceding example ``'width'``
  parameter sets TinyMCE widget width to 800 pixels without changing other configuration options.
- ``profile`` -- TinyMCE 4 configuration parameters. They **replace** the existing configuration.
  That is, you need to provide a fully defined TinyMCE configuration for ``profile`` parameter.

Also see the information about :ref:`form.media<forms-media>` template variable in the preceding sub-section.
