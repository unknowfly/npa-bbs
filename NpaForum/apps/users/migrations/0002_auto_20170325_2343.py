# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fav_node_nums',
            field=models.IntegerField(default=0, verbose_name='\u6536\u85cf\u8282\u70b9\u6570'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fav_topic_nums',
            field=models.IntegerField(default=0, verbose_name='\u6536\u85cf\u4e3b\u9898\u6570'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fav_user_nums',
            field=models.IntegerField(default=0, verbose_name='\u6536\u85cf\u7528\u6237\u6570'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='', max_length=200, upload_to='image/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
    ]