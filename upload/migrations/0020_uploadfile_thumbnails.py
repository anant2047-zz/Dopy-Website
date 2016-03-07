# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0019_auto_20160213_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='thumbnails',
            field=models.FileField(default='default', upload_to='temporary/thumbnails/'),
            preserve_default=False,
        ),
    ]
