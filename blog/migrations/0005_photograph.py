# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('image_file', models.ImageField(upload_to='%Y/%m/%d/')),
                ('description', models.TextField(null=True)),
                ('creted_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]
