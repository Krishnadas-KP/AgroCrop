# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_farmertransaction_l_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aadhaar_pic', models.FileField(upload_to=b'')),
                ('Field_Pic', models.FileField(upload_to=b'')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FarmerDetails')),
            ],
        ),
    ]
