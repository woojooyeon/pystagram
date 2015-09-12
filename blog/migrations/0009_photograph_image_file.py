# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_photograph_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='image_file',
            field=models.ImageField(upload_to='%Y/%m/%d/', default='django_conf_settings.png'),
            preserve_default=False,
        ),
    ]
