# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_photograph'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='image_url',
            field=models.URLField(default=datetime.datetime(2015, 9, 2, 12, 58, 25, 251455, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
