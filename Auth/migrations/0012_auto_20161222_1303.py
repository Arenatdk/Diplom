# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0011_auto_20161212_0339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='OSBBname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='addres',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='homenumber',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='street',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.CharField(choices=[(1, 'Resident'), (2, 'AdminOSBB')], default=1, max_length=2),
        ),
    ]
