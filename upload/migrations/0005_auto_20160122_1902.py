# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20160118_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='upload_file',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='panelImages',
            field=models.FileField(upload_to='Panel Images/', default=datetime.datetime(2016, 1, 22, 13, 31, 54, 672736, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='sliderImages',
            field=models.FileField(upload_to='Slider Images/', default='OK'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='storage',
            field=models.FileField(upload_to='Storage/', default=datetime.datetime(2016, 1, 22, 13, 32, 39, 389933, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
