# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20160123_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='thumbnails',
            field=models.FileField(upload_to='events/thumbnails', blank=True),
        ),
    ]
