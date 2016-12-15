# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('ctype', models.IntegerField(choices=[(1, 'Hiking'), (2, 'Camping'), (3, 'Sailing'), (4, 'Rowing'), (5, 'Skiing'), (6, 'Biking'), (7, 'Fishing'), (0, 'Other')], default=0)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('website', models.URLField(null=True, blank=True)),
                ('createdate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
