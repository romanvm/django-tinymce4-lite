Configuration
=============

The tinymce4-lite configuration options
---------------------------------------

The following options can be defined in your Django project's :file:`settings.py` file.

``TINYMCE_DEFAULT_CONFIG`` -- TinyMCE 4 widget configuration. tinymce4-lite provides reasonable default configuration
with essential editing capabilities, so you need to use this option only if you want to create your own custom
TinyMCE configuration. Default configuration::

  DEFAULT = {
      'selector': 'textarea',
      'theme': 'modern',
      'plugins': 'link image preview codesample contextmenu table code',
      'toolbar1': 'bold italic underline | alignleft aligncenter alignright alignjustify '
                 '| bullist numlist | outdent indent | table | link image | codesample | preview code',
      'contextmenu': 'formats | link image',
      'menubar': False,
      'inline': False,
      'statusbar': True,
      'height': 360,
  }

``TINYMCE_SPELLCHECKER`` -- enables spellchecker function for TinyMCE. For default configuration it also adds
a spellcheck button to TinyMCE toolbar. Default: ``False``.

``TINYMCE_FILEBROWSER`` -- enables file browser support in TinyMCE image and link dialogs.
tinymce4-lite supports both `django-filebrowser`_ and  `django-filebrowser-no-grappelli`_ file browsers.
Default: ``False``.

``TINYMCE_JS_URL`` -- a path to TinyMCE JavaScript library.
Default: :file:`{your_static_url}/tinymce/js/tinymce/tinymce.min.js`.
The following example shows how to load TinyMCE library from a CDN::

  TINYMCE_JS_URL = '//cdn.tinymce.com/4/tinymce.min.js'

``TINYMCE_CSS_URL`` -- a path to a CSS file with additional styles for TinyMCE.
Default styles are used to correct TinyMCE widget position in Django Admin interface.

``TINYMCE_CALLBACKS`` -- allows to define custom TinyMCE callbacks, for example ``file_browser_callback``
or ``spellchecker_callback``. This is a Python dictionary where keys are the names of callbacks and values are
valid JavaScript objects as Python strings. Default: ``{}`` (an empty :class:`dict`).
Read `TinyMCE documentation`_ about available callbacks.

.. note:: Custom ``file_browser_callback`` and ``spellchecker_callback`` options defined in ``TINYMCE_CALLBACKS``
  override tinymce4-lite built-in callbacks.

Language Configuration
----------------------

By default tinymce4-lite uses `LANGUAGE_CODE`_ and `LANGUAGES`_ Django options to automatically set up
TinyMCE interface language and available spellchecker dictionaries. That is why it is recommended
to define both options in your project's :file:`settings.py`.

``LANGUAGE_CODE`` option defines TinyMCE interface language and writing directionality.

``LANGUAGES`` option defines the list of available spellchecker languages. The first language in this list
is used as a default one. The list of spellchecker languages also depends on available **pyenchant** dictionaries.
For example, on Windows the default **pyenchant** installation includes only English, German and French spellchecker
dictionaries. Read `pyenchant documentation`_ to learn how to add additional spellchecker dictionaries.

Additional spellchecker dictionaries can be downloaded from `this page`_. Unpack a :file:`.sox` file
using an archive manager, for example `7zip`_, and copy :file:`.dic` and :file:`.aff` for your language into
**pyenchant**/**enchant** installation.

.. note:: Django language codes in ``LANGUAGES`` must match dictionary filenames.
  For example, ``'en-us'`` in ``LANGUAGES`` (with a country code)
  corresponds to :file:`en_US.dic`/:file:`en_US.aff` dictionary files,
  and ``'uk`` (no country code) corresponds to :file:`uk.dic`/:file:`uk.aff` dictionary files.

Also you can completely override TinyMCE automatic configuration by defining the necessary language options
in ``TINYMCE_DEFAULT_CONFIG``.

.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
.. _TinyMCE documentation: https://www.tinymce.com/docs/
.. _LANGUAGE_CODE: https://docs.djangoproject.com/en/1.9/ref/settings/#language-code
.. _LANGUAGES: https://docs.djangoproject.com/en/1.9/ref/settings/#languages
.. _pyenchant documentation: http://pythonhosted.org/pyenchant/tutorial.html#adding-language-dictionaries
.. _this page: http://www.softmaker.com/en/download/dictionaries
.. _7zip: http://www.7-zip.org/

