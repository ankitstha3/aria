# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Artist', models.CharField(max_length=250)),
                ('Album_title', models.CharField(max_length=500)),
                ('Genre', models.CharField(max_length=100)),
                ('album_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Soung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=250)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]
