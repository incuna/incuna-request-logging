# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user_pk', models.PositiveIntegerField()),
                ('registration_date', models.DateTimeField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.TextField()),
                ('request_method', models.CharField(max_length=255)),
            ],
        ),
    ]
