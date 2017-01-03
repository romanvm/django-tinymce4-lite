django-tinymce4-lite
====================

.. image:: https://travis-ci.org/romanvm/django-tinymce4-lite.svg?branch=master
  :target: https://travis-ci.org/romanvm/django-tinymce4-lite
.. image:: https://codecov.io/github/romanvm/django-tinymce4-lite/coverage.svg?branch=master
  :target: https://codecov.io/github/romanvm/django-tinymce4-lite?branch=master
.. image:: https://badge.fury.io/py/django.tinymce4-lite.svg
    :target: https://badge.fury.io/py/django.tinymce4-lite

**django-tinymce4-lite** is a reworked fork of `django-tinymce4`_. It provides a fully functional `TinyMCE 4`_
editor widget that can be used in Django forms and models.
The application can use `django-filebrowser`_ or `django-filebrowser-no-grappelli`_
as a file manager for TinyMCE 4 to insert images and file links into edited text.

**Warning**: TinyMCE 4 is incompatible with TinyMCE 3. Read `TinyMCE docs`_ for more information
about how to configure TimyMCE 4 editor widget.

Compatibility
-------------

- **Python**: 2.7, 3+
- **Django**: 1.8, 1.9, 1.10

Quick Start
===========

Install **django-tinymce4-lite**::

  $ pip install django-tinymce4-lite

Add ``tinymce`` to ``INSTALLED_APPS`` in ``settings.py`` for your Django project:

.. code-block:: python

  INSTALLED_APPS = (
      ...
      'tinymce',
  )

Add ``tinymce.urls`` to ``urls.py`` for your project:

.. code-block:: python

  urlpatterns = [
      ...
      url(r'^tinymce/', include('tinymce.urls')),
      ...
  ]

In your code:

.. code-block:: python

    from django.db import models
    from tinymce import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField('Content')

In Django Admin the widget is used automatically for all models that have ``HTMLField`` fields.
If you are using TinyMCE 4 in your website forms, add ``form.media`` variable into your templates:

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



Documentation
=============

http://romanvm.github.io/django-tinymce4-lite

License
=======

MIT license. See LICENSE.txt

.. _django-tinymce4: https://github.com/dani0805/django-tinymce4
.. _TinyMCE 4: https://www.tinymce.com/
.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _TinyMCE docs: https://www.tinymce.com/docs/
