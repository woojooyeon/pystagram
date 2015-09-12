# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20150822_0704'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(related_name='following_set', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='follower_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
