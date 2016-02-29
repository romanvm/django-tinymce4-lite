Welcome to django-tinymce4-lite documentation!
==============================================

**django-tinymce4-lite** is a reworked fork of `django-tinymce4`_. It provides a `TinyMCE 4`_
editor widget that can be used in Django forms and models.

In this fork all legacy and broken code has been cleaned in order to provide simple
but full-featured TinyMCE 4 experience in Django projects.

django-tinymce4-lite can use `django-filebrowser`_ or `django-filebrowser-no-grappelli`_
as a file manager for TinyMCE 4 to insert images and file links into edited text.
In addition to that, the application includes a spellchecker service for TinyMCE 4 spellchecker plugin.

Compatibility
-------------

- **Python**: 2.7, 3.4, 3.5
- **Django**: 1.8, 1.9

Naming Conventions
------------------

In this documentation **django-tinymce4-lite** or **tinymce4-lite** (all lowercase) refers to this
Python/Django application, and **TinyMCE 4** or **TinyMCE** (CamelCase) refers to
a JavaScript `TinyMCE`_ editor widget. If a version number is omitted, TinyMCE v.4.x.x is assumed.

.. _django-tinymce4: https://github.com/dani0805/django-tinymce4
.. _TinyMCE 4: https://www.tinymce.com/
.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _TinyMCE: https://www.tinymce.com/

Contents:

.. toctree::
  :maxdepth: 2

  installation
  configuration
  usage
  modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
