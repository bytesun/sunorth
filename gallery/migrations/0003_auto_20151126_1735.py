# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20151125_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(upload_to='gallery/%Y/%m/%d'),
        ),
    ]
