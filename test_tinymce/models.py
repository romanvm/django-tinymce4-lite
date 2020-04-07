from django.db import models
from django.urls import reverse
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
