# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 05:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20170529_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='slugger',
        ),
    ]
