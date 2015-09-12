# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_photograph_image_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photograph',
            old_name='creted_at',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='photograph',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', blank=True),
        ),
    ]
