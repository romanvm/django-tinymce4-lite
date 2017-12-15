from __future__ import absolute_import
from django.views.generic import CreateView, DetailView
from .models import TestModel


class TestCreateView(CreateView):
    template_name = 'test_tinymce/create.html'
    fields = ('content',)
    model = TestModel


class TestDisplayView(DetailView):
    template_name = 'test_tinymce/display.html'
    context_object_name = 'test_model'
    model = TestModel
