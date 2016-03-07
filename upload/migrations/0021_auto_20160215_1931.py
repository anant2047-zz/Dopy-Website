# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0020_uploadfile_thumbnails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='panelImages',
            field=models.FileField(null=True, blank=True, upload_to='temporary/panelImages/'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='thumbnails',
            field=models.FileField(null=True, blank=True, upload_to='temporary/thumbnails/'),
        ),
    ]
