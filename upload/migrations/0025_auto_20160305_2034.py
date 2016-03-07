# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0024_auto_20160305_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='year',
            field=models.CharField(default=2016, max_length=4, null=True),
        ),
    ]
