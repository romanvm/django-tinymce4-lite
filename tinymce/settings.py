# coding: utf-8

from __future__ import absolute_import
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.staticfiles.storage import staticfiles_storage

# Default TinyMCE 4 layout
DEFAULT = {
    'theme': 'modern',
    'plugins': 'link image',
    'toolbar': 'styleselect | bold italic underline | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | link image',
    'menubar': False,
    'inline': False,
    'statusbar': True,
    'height': 360,
}

JS_URL = staticfiles_storage.url('tinymce/js/tinymce/tinymce.min.js')
CSS_URL = getattr(settings, 'TINYMCE_CSS_URL', staticfiles_storage.url('tinymce/css/tinymce4.css'))
CALLBACKS = getattr(settings, 'TINYMCE_CALLBACKS', {})
USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)
USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER', False)
CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', DEFAULT)
if USE_SPELLCHECKER:
    DEFAULT['plugins'] += ' spellchecker'
    DEFAULT['toolbar'] += ' | spellchecker'
    if 'spellchecker_callback' not in CALLBACKS:
        CALLBACKS['spellchecker_callback'] = render_to_string('tinymce/spellchecker.js')
if USE_FILEBROWSER and 'file_browser_callback' not in CALLBACKS:
    CALLBACKS['file_browser_callback'] = 'djangoFileBrowser'
