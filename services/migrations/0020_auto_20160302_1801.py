# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_auto_20160215_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='panelImages',
            field=models.FileField(null=True, upload_to=b'/home/code_fanatic/dopy_rtm_build_1.1/dopy_media/temporary/panelImages', blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='thumbnails',
            field=models.FileField(null=True, upload_to=b'/home/code_fanatic/dopy_rtm_build_1.1/dopy_media/temporary/thumbnails', blank=True),
        ),
    ]
