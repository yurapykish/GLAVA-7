# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-27 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20170127_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ekzamyn',
            name='inspector',
        ),
    ]
