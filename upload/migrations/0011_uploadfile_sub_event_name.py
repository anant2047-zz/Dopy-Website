# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0010_auto_20160126_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='sub_event_name',
            field=models.CharField(max_length=120, blank=True, null=True),
        ),
    ]
