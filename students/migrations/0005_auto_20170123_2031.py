# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20170123_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='leader',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_group',
        ),
        migrations.DeleteModel(
            name='group',
        ),
    ]
