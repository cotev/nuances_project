# Generated by Django 2.0.6 on 2018-07-15 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCommonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Item', max_length=100)),
                ('author', models.CharField(default='Cotev', max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
    ]
