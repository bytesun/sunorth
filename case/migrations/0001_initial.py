# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(max_length=500)),
                ('tags', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
