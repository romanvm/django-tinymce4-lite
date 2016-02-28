from __future__ import absolute_import
from django.db import models
from tinymce import HTMLField


class TestModel(models.Model):
    """
    A model for testing TinyMCE 4 rendering
    """
    title = models.CharField(verbose_name='Title', max_length=100)
    content = HTMLField(verbose_name='Content')
