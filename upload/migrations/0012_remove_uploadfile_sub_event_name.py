# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0011_uploadfile_sub_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='sub_event_name',
        ),
    ]
