from django.db import models

class Todo(models.Model):
    title = models.CharField( max_length=255)
    finished = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
