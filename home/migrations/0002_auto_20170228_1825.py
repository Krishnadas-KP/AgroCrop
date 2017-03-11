# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Rate', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Transaction_Date', models.DateTimeField(auto_now_add=True)),
                ('Item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Price')),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Transaction_Date', models.DateTimeField(auto_now_add=True)),
                ('Item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Price')),
                ('dest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='home.Local')),
                ('src', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='home.Local')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Price')),
                ('L_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Local')),
            ],
        ),
        migrations.RenameField(
            model_name='farmertransaction',
            old_name='Quanity',
            new_name='Quantity',
        ),
    ]