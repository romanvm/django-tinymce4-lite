from __future__ import absolute_import
from django.contrib import admin
from .models import TestModel, TestChildModel


class ChildInline(admin.StackedInline):
    model = TestChildModel
    extra = 1


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    inlines = [ChildInline]

