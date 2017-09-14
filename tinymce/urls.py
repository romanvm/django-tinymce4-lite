# coding: utf-8

from __future__ import absolute_import
from django.conf.urls import url
from .views import spell_check, filebrowser, css, spell_check_callback

urlpatterns = [
    url(r'^spellchecker/$', spell_check, name='tinymce-spellchecker'),
    url(r'^filebrowser/$', filebrowser, name='tinymce-filebrowser'),
    url(r'^tinymce4.css', css, name='tinymce-css'),
    url(r'^spellcheck-callback.js', spell_check_callback, name='tinymce-spellcheck-callback')
]
