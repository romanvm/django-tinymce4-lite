from __future__ import absolute_import
from django.views.generic import TemplateView, CreateView
from .models import TestModel


class TestIndexView(TemplateView):
    template_name = 'tinymce_tests/index.html'


class TestCreateView(CreateView):
    template_name = 'tinymce_tests/create.html'
    fields = ('title', 'content')
    model = TestModel
