# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20161107_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='language',
            field=models.CharField(max_length=10, default='zh-cn'),
        ),
    ]
