# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170326_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='\u4e2a\u4eba\u7f51\u7ad9'),
        ),
    ]
