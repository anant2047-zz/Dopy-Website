# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0022_auto_20160215_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='panelImages',
            field=models.FileField(upload_to=b'/home/code_fanatic/dopy_rtm_build_1.1/dopy_media/temporary/panelImages'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='thumbnails',
            field=models.FileField(upload_to=b'/home/code_fanatic/dopy_rtm_build_1.1/dopy_media/temporary/thumbnails'),
        ),
    ]
