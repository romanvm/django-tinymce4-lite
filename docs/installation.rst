Installation
============

Install **django-tinymce4-lite** from the GitHub repo::

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

For TinyMCE spellchecker plugin you need to install `pyenchant`_ package and add the necessary spelling dictionaries,
if they are missing from pyenchant default installation on your system.
On some Linux systems you may need to install ``enchant`` libraries prior to installing ``pyenchant``.
For example, on Debian/Ubuntu use the following command::

  $ sudo apt-get install enchant

Read :ref:`"Language Configuration"<language_config>` subsection about configuring the **tinymce4-lite** spellchecker.

.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _django-filebrowser documentation: https://django-filebrowser.readthedocs.org/en/latest/
.. _pyenchant: http://pythonhosted.org/pyenchant/
