# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20160213_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='event_name',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='link',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='sliderImages',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='thumbnails',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='year',
        ),
    ]
