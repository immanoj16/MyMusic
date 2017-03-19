from __future__ import unicode_literals

from django.db import models
import datetime


class Band(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.CharField(max_length=250, null=True, blank=True)
    date_added = models.DateTimeField(default=datetime.datetime.now())
    date_formed = models.DateField(null=True, blank=True)
    date_disbanded = models.DateField(null=True, blank=True)
    origin = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(max_length=5000, null=True, blank=True)
