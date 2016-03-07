# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0015_auto_20160213_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='year',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='link',
            field=models.CharField(default='NOT FOUND', blank=True, max_length=240),
        ),
    ]
