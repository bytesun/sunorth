# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0005_auto_20161107_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='do_time',
            field=models.DateField(),
        ),
    ]
