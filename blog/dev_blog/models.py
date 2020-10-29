from django.contrib import admin
from django.db import models
from datetime import datetime


class Entry(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200)
    body = models.CharField(max_length=20000)
    created_on = models.DateField(datetime.now())
    
    def __str__(self):
        return self.title

admin.site.register(Entry)