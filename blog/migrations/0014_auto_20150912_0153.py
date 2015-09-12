# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import my_pystagram.validators
import my_pystagram.file


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150905_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=my_pystagram.file.random_name_with_file_field, validators=[my_pystagram.validators.jpeg_validator], blank=True, null=True),
        ),
    ]
