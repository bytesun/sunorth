# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('story', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=50)),
                ('rate', models.IntegerField(default=0)),
                ('createtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('photographer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
