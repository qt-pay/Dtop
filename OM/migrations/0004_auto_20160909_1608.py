# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-09 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OM', '0003_cmdhistory_client_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverlist',
            name='service_owner',
            field=models.ForeignKey(default='00001', on_delete=django.db.models.deletion.CASCADE, to='OM.ServerGroup', verbose_name='\u670d\u52a1\u5668\u5c5e\u7ec4'),
        ),
    ]