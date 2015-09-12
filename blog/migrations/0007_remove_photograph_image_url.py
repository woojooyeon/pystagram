# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_photograph_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photograph',
            name='image_url',
        ),
    ]
