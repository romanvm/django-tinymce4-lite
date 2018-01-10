from __future__ import absolute_import
from django.db import models
try:
    from django.urls import reverse, reverse
except ImportError:
    from django.core.urlresolvers import reverse
from tinymce import HTMLField


class TestModel(models.Model):
    """
    A model for testing TinyMCE 4 rendering
    """
    content = HTMLField(verbose_name='HTML Content')

    def get_absolute_url(self):
        return reverse('display', kwargs={'pk': self.pk})


class TestChildModel(models.Model):
    """
    A model for testing TinyMCE 4 rendering in admin inlines
    """
    content = HTMLField(verbose_name='HTML Child Content')
    parent = models.ForeignKey(TestModel, on_delete=models.CASCADE)
