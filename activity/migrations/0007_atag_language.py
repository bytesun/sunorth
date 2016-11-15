# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_auto_20161107_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='atag',
            name='language',
            field=models.CharField(max_length=10, default='zh-cn'),
        ),
    ]
