# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0008_auto_20170226_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='do_time',
            field=models.DateField(null=True),
        ),
    ]
