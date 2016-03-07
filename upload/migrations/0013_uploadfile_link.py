# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0012_remove_uploadfile_sub_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='link',
            field=models.CharField(max_length=240, default='https://www.google.co.in/drive/'),
            preserve_default=False,
        ),
    ]
