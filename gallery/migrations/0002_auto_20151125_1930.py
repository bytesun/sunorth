# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='tags',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(upload_to='gallery/%Y/%m/%d'),
        ),
    ]
