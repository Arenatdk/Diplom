# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0009_auto_20161212_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.Level'),
        ),
        migrations.AlterField(
            model_name='level',
            name='podezd',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.Podezd'),
        ),
    ]
