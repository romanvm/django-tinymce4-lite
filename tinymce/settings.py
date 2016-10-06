# coding: utf-8
# License: MIT, see LICENSE.txt
"""The django-tinymce4-lite configuration options"""

from __future__ import absolute_import
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

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
"""Default TinyMCE 4 configuration"""
USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)
"""Use tinymce4 built-in spellchecker service"""
if USE_SPELLCHECKER:
    DEFAULT['plugins'] += ' spellchecker'
    DEFAULT['toolbar1'] += ' | spellchecker'
CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', DEFAULT)
"""TinyMCE 4 configuration"""
JS_URL = getattr(settings, 'TINYMCE_JS_URL', staticfiles_storage.url('tinymce/js/tinymce/tinymce.min.js'))
"""TinyMCE 4 JavaScript code"""
ADDIONAL_JS_URLS = getattr(settings, 'TINYMCE_ADDITIONAL_JS_URLS', None)
"""Additional JS files for TinyMCE (e.g. custom plugins)"""
CSS_URL = getattr(settings, 'TINYMCE_CSS_URL', None)
"""
Additional CSS styles for TinyMCE 4

The default CSS is used to fix TinyMCE 4 position in Django Admin.
"""
CALLBACKS = getattr(settings, 'TINYMCE_CALLBACKS', {})
"""TinyMCE 4 calback JavaScript functions"""
USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER', 'filebrowser' in settings.INSTALLED_APPS)
"""
Enable integration with django-filebrowser

Both `django-filebrowser`_ and `django-filebrowser-no-grappelli`_ are supported.

.. _django-filebrowser: https://github.com/sehmaschine/django-filebrowser
.. _django-filebrowser-no-grappelli: https://github.com/smacker/django-filebrowser-no-grappelli
"""
