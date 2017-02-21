# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-21 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_auto_20170220_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni_data',
            name='batch',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='alumni_data',
            name='flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alumni_data',
            name='github_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='alumni_data',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='alumni_data',
            name='skill',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='alumni_data',
            name='photo',
            field=models.ImageField(default='default.png', upload_to='alumni_images/'),
        ),
    ]
