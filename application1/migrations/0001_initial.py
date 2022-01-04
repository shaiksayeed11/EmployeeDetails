# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-12-07 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=25)),
                ('esal', models.FloatField()),
                ('design', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('join_date', models.DateField()),
                ('company', models.CharField(max_length=25)),
            ],
        ),
    ]
