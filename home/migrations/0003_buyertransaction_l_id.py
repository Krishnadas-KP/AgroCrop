# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170228_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyertransaction',
            name='L_id',
            field=models.ForeignKey(default='L0001', on_delete=django.db.models.deletion.CASCADE, to='home.Local'),
            preserve_default=False,
        ),
    ]
