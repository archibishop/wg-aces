# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-21 15:09
from __future__ import unicode_literals

from django.db import migrations

def authors(apps, schema_editor):
    # We can't import the models directly as it may be a newer
    # version than this migration expects. We use the historical version.
    LicenseAuthor = apps.get_model('core', 'LicenseAuthor')
    Exercise = apps.get_model('exercises', 'Exercise')
    for exercise in Exercise.objects.all():
        author, created = LicenseAuthor.objects.get_or_create(author_name=exercise.license_author)
        Exercise.objects.filter(pk=exercise.id).update(license_author_link_id=author)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180821_1041'),
        ('exercises', '0007_auto_20180821_1041'),
        
    ]

    operations = [
        migrations.RunPython(authors),
    ]
