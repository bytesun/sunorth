# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_remove_activity_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='language',
            field=models.CharField(max_length=10, default='zh-cn'),
        ),
    ]
