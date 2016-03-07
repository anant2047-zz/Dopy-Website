# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0021_auto_20160215_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='panelImages',
            field=models.FileField(default='not found', upload_to='temporary/panelImages/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='thumbnails',
            field=models.FileField(upload_to='temporary/thumbnails/'),
        ),
    ]
