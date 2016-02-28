django-tinymce4-lite
====================

.. image:: https://travis-ci.org/romanvm/django-tinymce4-lite.svg?branch=master
  :target: https://travis-ci.org/romanvm/django-tinymce4-lite
.. image:: https://codecov.io/github/romanvm/django-tinymce4-lite/coverage.svg?branch=master
  :target: https://codecov.io/github/romanvm/django-tinymce4-lite?branch=master
.. image:: https://www.quantifiedcode.com/api/v1/project/48b63a65324642af823606c3c0444395/badge.svg
  :target: https://www.quantifiedcode.com/app/project/48b63a65324642af823606c3c0444395
  :alt: Code issues

django-tinymce4-lite is a remade fork of `django-tinymce4`_. It provides a fully functional `TinyMCE 4`_ editor widget
that can be used in Django forms and models. The application can use
`django-filebrowser`_ or `django-filebrowser-no-grappelli`_ as a file manager for TinyMCE 4 to insert images and
file links into edited text.

**Warning**: TinyMCE 4 is incompatible with TinyMCE 3. Read `TinyMCE docs`_ for more information
about how to configure TimyMCE 4 editor.

Compatibility
-------------

**Python**: 2.7, 3.4, 3.5
**Django**: 1.8, 1.9

Quick Start
===========

(The application is fully functional. I need to complete docs and a PyPI package.)

Install requirements:

    $ pip install -r requirements.txt

Copy ``tinymce`` folder to your ``PYTHONPATH``.

Add ``tinymce`` to ``INSTALLED_APPS`` in ``settings.py`` for your project::

    INSTALLED_APPS = (
        ...
        'tinymce',
    )

Add ``tinymce.urls`` to ``urls.py`` for your project::

    urlpatterns = patterns('',
        ...
        (r'^tinymce/', include('tinymce.urls')),
    )

In your code::

    from django.db import models
    from tinymce import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField('Content')

In your templates (if you are using TinyMCE 4 in your site forms):

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


Documentation
=============

TBD

License
=======

MIT. See LICENSE.txt

.. _django-tinymce4: https://github.com/dani0805/django-tinymce4
.. _TinyMCE 4: https://www.tinymce.com/
.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _TinyMCE docs: https://www.tinymce.com/docs/

