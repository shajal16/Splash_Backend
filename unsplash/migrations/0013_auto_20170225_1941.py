# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-25 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unsplash', '0012_auto_20170225_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='exif_aparture',
            new_name='exif_aperture',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='exif_focul',
            new_name='exif_focal',
        ),
    ]
