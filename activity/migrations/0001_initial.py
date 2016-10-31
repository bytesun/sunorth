# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('subject', models.CharField(max_length=500)),
                ('tags', models.CharField(max_length=500)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('do_time', models.DateTimeField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comment', models.TextField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('activity', models.ForeignKey(to='activity.Activity')),
                ('owner', models.ForeignKey(related_name='activity_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
