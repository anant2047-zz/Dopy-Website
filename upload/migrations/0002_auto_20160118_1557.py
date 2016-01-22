# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventName',
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='event_name',
            field=models.CharField(default=datetime.datetime(2016, 1, 18, 10, 27, 48, 906025, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]
