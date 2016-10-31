# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blog_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='language',
            field=models.CharField(max_length=10, default='zh-cn'),
        ),
    ]
