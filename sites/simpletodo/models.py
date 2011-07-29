from django.db import models
from django.contrib import admin

class Todo(models.Model):
    title = models.CharField( max_length=255)
    finished = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class TodoAdmin(admin.ModelAdmin):
    list_display        = ('title', 'finished')
    search_fields       = ('title',)

admin.site.register(Todo, TodoAdmin)
