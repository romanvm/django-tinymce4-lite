Configuration
=============

Application Configuration
-------------------------

The following options can be defined for **tinymce4-lite** in your Django project's
:file:`settings.py` file.

.. _TINYMCE_DEFAULT_CONFIG:

``TINYMCE_DEFAULT_CONFIG`` -- TinyMCE 4 widget configuration.
**tinymce4-lite** provides a reasonable default configuration with essential editing capabilities,
so you need to use this option only if you want to create your own custom TinyMCE configuration.

.. note:: In **tinymce4-lite** the TinyMCE configuration is defined as a Python :class:`dict`.
  The :class:`dict` configuration is then translated to JSON configuration
  according to :class:`json.JSONEncoder` rules.

See `TinyMCE documentation`_ for available configuration options.

Default configuration::

  DEFAULT = {
      'selector': 'textarea',
      'theme': 'modern',
      'plugins': 'link image preview codesample contextmenu table code lists',
      'toolbar1': 'formatselect | bold italic underline | alignleft aligncenter alignright alignjustify '
                 '| bullist numlist | outdent indent | table | link image | codesample | preview code',
      'contextmenu': 'formats | link image',
      'menubar': False,
      'inline': False,
      'statusbar': True,
      'width': 'auto',
      'height': 360,
  }

``TINYMCE_SPELLCHECKER`` -- enables spellchecker function for TinyMCE. For the default configuration it also adds
a spellcheck button to TinyMCE toolbar. Default: ``False``.

.. note:: If you are using a custom TinyMCE configuration, don't forget to add `spellchecker`_ plugin to
  your configuration, and add the necessary menu item/toolbar button. Also read `Language Configuration`_
  subsection about how to configure the spellchecker.

``TINYMCE_FILEBROWSER`` -- enables file browser support in TinyMCE image and link dialogs.
**tinymce4-lite** supports `django-filebrowser-no-grappelli`_ file browser.
Default: ``True`` if ``'filebrowser'`` is added to `INSTALLED_APPS`_, else ``False``.

``TINYMCE_JS_URL`` -- a path to TinyMCE JavaScript library.
Default: :file:`{your_static_url}/tinymce/js/tinymce/tinymce.min.js`.
The following example shows how to load the TinyMCE library from a CDN::

  TINYMCE_JS_URL = '//cdn.tinymce.com/4/tinymce.min.js'

``TINYMCE_ADDITIONAL_JS_URLS`` -- a :class:`list` of URLs for additional JavaScript files to be used with the TinyMCE
widget, for example, custom TinyMCE plugins. Default: ``None``.

``TINYMCE_CSS_URL`` -- a path to a CSS file with additional styles for TinyMCE. Unlike
``content_style`` and ``content_css`` TinyMCE settings (see ":ref:`Applying custom CSS<custom-css>`"),
this CSS is applied to the TinyMCE widget itself, for example to correct the widget position on a page.
Default: ``None``.

``TINYMCE_CALLBACKS`` -- allows to define custom TinyMCE callbacks, for example ``file_browser_callback``
or ``spellchecker_callback``. This is a Python :class:`dict` where keys are the names of callbacks and values are
JavaScript objects as Python strings. Default: ``{}`` (an empty :class:`dict`).
Read `TinyMCE documentation`_ to learn about available callbacks.

.. note:: Custom ``file_browser_callback`` and ``spellchecker_callback`` options defined in ``TINYMCE_CALLBACKS``
  override **tinymce4-lite** built-in callbacks.

.. _language_config:

Language Configuration
----------------------

By default **tinymce4-lite** uses `LANGUAGE_CODE`_ and `LANGUAGES`_ Django options to automatically set up
TinyMCE interface language and available spellchecker dictionaries. That is why it is recommended
to define both options in your project's :file:`settings.py`.

``LANGUAGE_CODE`` option defines TinyMCE interface language and writing directionality.

``LANGUAGES`` option defines the list of available spellchecker languages. The first language in this list
is used as the default one. The list of spellchecker languages also depends on available **pyenchant** dictionaries.
For example, on Windows the default **pyenchant** installation includes only English, German and French spellchecker
dictionaries. You can view the list available spellchecker dictionaries by running ``enchant.list_languages()`` function in a console
from your working Python environment. For example::

  >>> import enchant
  >>> enchant.list_languages()
  ['de_DE', 'en_AU', 'en_GB', 'en_US', 'fr_FR']


On Linux you can install `Hunspell`_ dictionaries for your languages
that will be automatically used by **pyenchant**.
E.g. for Ukrainian spelling dictionary on Ubuntu/Debian::

  $ sudo apt install hunspell-uk

On Windows you need to add the necessary dictionaries manually to **enchant** package
in ``site-packages`` directory of your working Python environment.
Additional spellchecker dictionaries can be downloaded from `this page`_. Unpack a :file:`.sox` file
using an archive manager, for example `7zip`_, and copy :file:`.dic` and :file:`.aff` for your language to
``enchant/share/enchant/myspell/`` directory inside **enchant** package.

.. note:: Django language codes in ``LANGUAGES`` must match dictionary filenames.
  For example, ``'en-us'`` in ``LANGUAGES`` (with a country code)
  corresponds to :file:`en_US.dic`/:file:`en_US.aff` dictionary files,
  and ``'uk'`` (no country code) corresponds to :file:`uk.dic`/:file:`uk.aff` dictionary files.

Also you can completely override TinyMCE automatic language configuration by defining the necessary language options
in `TINYMCE_DEFAULT_CONFIG`_.

.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _TinyMCE documentation: https://www.tinymce.com/docs/
.. _LANGUAGE_CODE: https://docs.djangoproject.com/en/2.0/ref/settings/#language-code
.. _LANGUAGES: https://docs.djangoproject.com/en/2.0/ref/settings/#languages
.. _pyenchant documentation: http://pythonhosted.org/pyenchant/tutorial.html#adding-language-dictionaries
.. _this page: http://www.softmaker.com/en/download/dictionaries
.. _7zip: http://www.7-zip.org/
.. _INSTALLED_APPS: https://docs.djangoproject.com/en/2.0/ref/settings/#installed-apps
.. _spellchecker: https://www.tinymce.com/docs/plugins/spellchecker/
.. _Hunspell: http://hunspell.github.io
