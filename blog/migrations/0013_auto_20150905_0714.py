# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import my_pystagram.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='', validators=[my_pystagram.validators.jpeg_validator], blank=True),
        ),
    ]
