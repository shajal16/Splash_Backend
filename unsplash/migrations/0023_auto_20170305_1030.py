# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-05 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unsplash', '0022_photo_curated_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CuratedList',
            new_name='CollectionList',
        ),
    ]
