# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20170329_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routes',
            name='Item_id',
        ),
        migrations.AddField(
            model_name='routes',
            name='Item_Name',
            field=models.CharField(default='xxy', max_length=50),
            preserve_default=False,
        ),
    ]