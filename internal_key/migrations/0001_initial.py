# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-06 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='internal_key_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=200, null=True)),
                ('value', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
