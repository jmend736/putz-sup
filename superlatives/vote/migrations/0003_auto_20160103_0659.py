# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20160103_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='ans_sub',
        ),
        migrations.AddField(
            model_name='answer',
            name='ans_sub',
            field=models.ManyToManyField(to='vote.Submitter'),
        ),
    ]