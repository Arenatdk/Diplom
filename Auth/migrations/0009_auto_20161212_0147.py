# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0008_level_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeber', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='level',
            old_name='number',
            new_name='level_number',
        ),
        migrations.AddField(
            model_name='apartment',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.Level'),
        ),
    ]