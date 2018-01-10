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


If you want to use `django-filebrowser-no-grappelli`_ file manager,
install this package. Refer to `django-filebrowser documentation`_ to learn
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

Upgrade
-------

It is strongly recommended to upgrade `tinymce4-lite` by specifying the exact
application version you want to upgrade to::

  $ pip install django-tinymce4-lite==X.Y.Z

Unless you are loading TinyMCE 4 from a CDN, after upgrading you need to run
Django's ``collectstatic`` command to update TinyMCE 4 static files in your
folder where your project's static files are served from::

  $ python manage.py collectstatic


.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _django-filebrowser documentation: https://django-filebrowser.readthedocs.org/en/latest/
.. _pyenchant: http://pythonhosted.org/pyenchant/
