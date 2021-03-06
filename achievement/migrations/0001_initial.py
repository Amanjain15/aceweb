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
            name='academics_achievement_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='default.png', upload_to='achievemnt_images/')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cocurricular_achievement_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='default.png', upload_to='achievemnt_images/')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='overall_achievement_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='default.png', upload_to='achievemnt_images/')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='training_placement_achievement_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='default.png', upload_to='achievemnt_images/')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
