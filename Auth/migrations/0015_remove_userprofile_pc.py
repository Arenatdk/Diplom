# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 11:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0014_userprofile_pc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='pc',
        ),
    ]
