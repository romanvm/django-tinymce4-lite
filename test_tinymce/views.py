from __future__ import absolute_import
from django.views.generic import TemplateView, CreateView
from .models import TestModel


class TestIndexView(TemplateView):
    template_name = 'test_tinymce/index.html'


class TestCreateView(CreateView):
    template_name = 'test_tinymce/create.html'
    fields = ('title', 'content')
    model = TestModel
