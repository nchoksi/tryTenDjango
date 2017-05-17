from __future__ import unicode_literals


from django.db import models


class profile(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(default='description default text')

    def __unicode__(self):
        return self.name

