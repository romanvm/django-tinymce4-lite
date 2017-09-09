Installation
============

Install **django-tinymce4-lite** from PyPI::

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


If you want to use `django-filebrowser`_ or `django-filebrowser-no-grappelli`_ file manager,
install one of those packages. Refer to `django-filebrowser documentation`_ to learn
how to install and configure the filebrowser application.

For TinyMCE spellchecker plugin you need to install `pyenchant`_ package::

  $ pip install pyenchant

On some Linux systems you may also need to install binary ``enchant`` libraries
prior to installing ``pyenchant``.
For example, on Debian/Ubuntu use the following command::

  $ sudo apt-get install enchant

Also you need to add the necessary spelling dictionaries
if they are missing from ``pyenchant`` default installation on your system.

Read :ref:`"Language Configuration"<language_config>` subsection about configuring
the **tinymce4-lite** spellchecker.

.. note:: If you are using :class:`django.contrib.staticfiles.storage.ManifestStaticFilesStorage`
  for static files and need to collect static files for your Django deployment,
  you have to temporarily switch to ``DEBUG = True`` in your project's settings
  before running ``collectstatic`` command, and then switch to ``DEBUG = False``
  back again. This will allow to correctly create hash-versioned static files and
  ``manifest.json``.

Upgrade
-------

It is recommended to upgrade `tinymce4-lite` by specifying the exact
application version::

  $ pip install django-tinymce4-lite==X.Y.Z

Unless you are loading TinyMCE 4 from a CDN, after upgrading you need to run
Django's ``collectstatic`` command to update TinyMCE 4 static files in your
folder where your project's static files are served from::

  $ python manage.py collectstatic

See information about ``ManifestStaticFilesStorage`` in the preceding sub-section.

.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _django-filebrowser documentation: https://django-filebrowser.readthedocs.org/en/latest/
.. _pyenchant: http://pythonhosted.org/pyenchant/
