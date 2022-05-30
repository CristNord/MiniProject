# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-05-26 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20220526_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='blog_pic',
            field=models.ImageField(blank=True, null=True, upload_to='blog_pics'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]