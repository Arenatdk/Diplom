# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-12 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_apartment_subsidyi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='subsidyi',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.subsidyi'),
        ),
    ]