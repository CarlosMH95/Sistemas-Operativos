# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class News(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    story = models.CharField(max_length=255, blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    time_stamp = models.CharField(max_length=255, blank=True, null=True)
    numero_accessos = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'news'