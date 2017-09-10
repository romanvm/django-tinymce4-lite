from __future__ import absolute_import
from django.contrib import admin
from .models import TestModel, ChildTestModel

class ChildTestModelInlineAdmin(admin.StackedInline):
    model = ChildTestModel
    extra = 1

@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    model = TestModel
    inlines = [ChildTestModelInlineAdmin]
