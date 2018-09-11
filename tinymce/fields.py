from django import forms
from django.contrib.postgres.forms import SplitArrayField
from .widgets import SplitArrayTinyMCEWidget, TinyMCE


class SplitArrayTinyMCEField(SplitArrayField):
    def __init__(self, size, remove_trailing_nulls=False, attrs=None,
                 mce_attrs=None, profile=None,  **kwargs):
        self.base_field = forms.CharField(widget=TinyMCE(attrs, mce_attrs,
                                                         profile))
        self.size = size
        self.remove_trailing_nulls = remove_trailing_nulls
        widget = SplitArrayTinyMCEWidget(widget=self.base_field.widget,
                                         size=size)
        kwargs.setdefault('widget', widget)
        forms.Field.__init__(self, **kwargs)
