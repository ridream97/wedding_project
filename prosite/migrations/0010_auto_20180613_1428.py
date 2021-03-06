# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prosite', '0009_auto_20180613_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('id_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prosite.Block')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='id_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prosite.Block'),
        ),
    ]
