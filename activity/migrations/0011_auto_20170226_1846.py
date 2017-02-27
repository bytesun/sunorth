# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0010_auto_20170226_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='tags',
            field=models.ManyToManyField(to='activity.ATag', null=True),
        ),
    ]
