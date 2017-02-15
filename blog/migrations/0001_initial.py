# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('auther', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date of publication')),
            ],
        ),
        migrations.CreateModel(
            name='StoryPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageNumber', models.IntegerField(blank=True, null=True)),
                ('page', models.ImageField(upload_to='pages/')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Story')),
            ],
        ),
    ]
