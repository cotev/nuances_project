# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_storypage_pagetitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storypage',
            name='pageTitle',
            field=models.CharField(max_length=100),
        ),
    ]
