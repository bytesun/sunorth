# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_activity_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='language',
        ),
    ]
