# coding: utf-8

from django.conf.urls import url
from tinymce.views import spell_check, filebrowser, css

urlpatterns = [
    url(r'^spellchecker/$', spell_check, name='tinymce-spellchecker'),
    url(r'^filebrowser/$', filebrowser, name='tinymce-filebrowser'),
    url(r'^css/$', css, name='tinymce-css'),
]
