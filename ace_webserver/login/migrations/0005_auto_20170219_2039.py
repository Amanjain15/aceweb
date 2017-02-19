# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-19 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170219_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_data',
            name='group_id',
            field=models.SmallIntegerField(choices=[(1, 'student'), (2, 'faculty'), (3, 'alumni'), (4, 'admin'), (5, 'developer')], default=0),
        ),
    ]
