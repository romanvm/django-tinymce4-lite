# coding: utf-8

from __future__ import absolute_import
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

# Default TinyMCE 4 layout
DEFAULT = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': 'link image preview codesample',
    'toolbar1': 'styleselect | bold italic | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | link image | codesample | preview',
    'menubar': False,
    'inline': False,
    'statusbar': True,
    'height': 360,
}

JS_URL = staticfiles_storage.url('tinymce/js/tinymce/tinymce.min.js')
CSS_URL = getattr(settings, 'TINYMCE_CSS_URL', None)
CALLBACKS = getattr(settings, 'TINYMCE_CALLBACKS', {})
USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)
USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER', False)
CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', DEFAULT)
if USE_SPELLCHECKER:
    DEFAULT['plugins'] += ' spellchecker'
    DEFAULT['toolbar1'] += ' | spellchecker'
