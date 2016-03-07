# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0016_auto_20160213_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='home_slider',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='sliderImages',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='storage',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='thumbnails',
        ),
    ]
