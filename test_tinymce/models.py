from __future__ import absolute_import
from django.db import models
from tinymce import HTMLField

class TestModel(models.Model):
    """
    A model for testing TinyMCE 4 rendering
    """
    content = HTMLField(verbose_name='HTML Content')

class ChildTestModel(models.Model):
    """
    A model for testing TinyMCE 4 rendering inline in django admin
    """
    content = HTMLField(verbose_name='HTML Content')
    test_model = models.ForeignKey(TestModel)
