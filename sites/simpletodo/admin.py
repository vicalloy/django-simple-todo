#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.contrib import admin

from models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display        = ('title', 'finished')
    search_fields       = ('title',)

admin.site.register(Todo, TodoAdmin)
