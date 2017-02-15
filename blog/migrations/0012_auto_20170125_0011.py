# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-25 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170124_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentSketch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Anonymous', max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date of comment')),
                ('sketch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Sketch')),
            ],
        ),
        migrations.CreateModel(
            name='CommentStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Anonymous', max_length=100)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date of comment')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Story')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='sketch',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='story',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
