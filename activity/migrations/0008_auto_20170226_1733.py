# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_atag_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 27, 1, 32, 42, 313862, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='organizer',
            field=models.CharField(default=datetime.datetime(2017, 2, 27, 1, 33, 25, 362868, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='participants',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='activity',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 27, 1, 33, 32, 417409, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='language',
            field=models.CharField(default='en-us', max_length=10),
        ),
    ]
