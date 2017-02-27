# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0009_auto_20170226_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='activity',
            name='organizer',
            field=models.CharField(max_length=50, default='xxx@sunorth.org'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
