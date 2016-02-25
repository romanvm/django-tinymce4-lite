# coding: utf-8
# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

from __future__ import absolute_import
from django.db import models
from django.contrib.admin.widgets import AdminTextareaWidget
from tinymce.widgets import TinyMCE, AdminTinyMCE


class HTMLField(models.TextField):
    """
    A text area field for HTML content.

    It uses the TinyMCE 4 widget in forms.
    """
    def __init__(self, *args, **kwargs):
        self.tinymce_profile = kwargs.pop('profile', None)
        super(HTMLField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'widget': TinyMCE(profile=self.tinymce_profile)
        }
        defaults.update(kwargs)
        # As an ugly hack, we override the admin widget
        if defaults['widget'] == AdminTextareaWidget:
            defaults['widget'] = AdminTinyMCE(profile=self.tinymce_profile)
        return super(HTMLField, self).formfield(**defaults)
