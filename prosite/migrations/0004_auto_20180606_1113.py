# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 08:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prosite', '0003_album_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
    ]