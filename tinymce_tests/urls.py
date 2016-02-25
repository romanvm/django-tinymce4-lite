# coding: utf-8
# Author: Roman Miroshnychenko aka Roman V.M. (romanvm@yandex.ua)

from __future__ import absolute_import
from django.conf.urls import url
from .views import TestIndexView, TestCreateView

urlpatterns = [
    url(r'^$', TestIndexView.as_view(), name='index'),
    url(r'^add-object/$', TestCreateView.as_view(), name='create')
]
