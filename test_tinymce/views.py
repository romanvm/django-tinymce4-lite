from __future__ import absolute_import
from django.views.generic import CreateView
from .models import TestModel


class TestCreateView(CreateView):
    template_name = 'test_tinymce/create.html'
    fields = ('content',)
    model = TestModel
