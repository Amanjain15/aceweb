# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-21 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_key', '0003_auto_20170220_1827'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='custom_keys_data',
            new_name='custom_key_data',
        ),
    ]
