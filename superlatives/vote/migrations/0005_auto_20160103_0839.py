# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20160103_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans_quest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vote.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans_sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Submitter'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quest_sub',
            field=models.ManyToManyField(null=True, to='vote.Submitter', verbose_name='Submitter'),
        ),
    ]
