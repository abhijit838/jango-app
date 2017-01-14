# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-14 08:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 14, 8, 46, 54, 910922, tzinfo=utc)),
        ),
    ]
