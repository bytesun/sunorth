# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_activity_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='tags',
        ),
        migrations.AddField(
            model_name='activity',
            name='tags',
            field=models.ManyToManyField(to='activity.ATag'),
        ),
    ]
