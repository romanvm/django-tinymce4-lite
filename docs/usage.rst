Usage
=====

Model HTMLField
---------------

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

If you are using TinyMCE 4 in your website forms, you need to add ``form.media`` variable
to the ``<head>`` section of your templates:

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

In Django Admin interface the widget is used automatically for all models that have
:class:`HTMLField<tinymce.HTMLField>` fields.
