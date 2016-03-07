# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0006_auto_20160215_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='sliderImages',
            field=models.FileField(null=True, upload_to=b'/home/code_fanatic/dopy_rtm_build_1.1/dopy_media/temporary/sliderImages', blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='thumbnails',
            field=models.FileField(null=True, upload_to=b'/home/code_fanatic/dopy_rtm_build_1.1/dopy_media/temporary/thumbnails', blank=True),
        ),
    ]
