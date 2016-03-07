# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0023_auto_20160302_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='link',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='link_day_one',
            field=models.CharField(default=b'', max_length=240, blank=True),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='link_day_three',
            field=models.CharField(default=b'', max_length=240, blank=True),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='link_day_two',
            field=models.CharField(default=b'', max_length=240, blank=True),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='link_day_zero',
            field=models.CharField(default=b'', max_length=240, blank=True),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='fest_name',
            field=models.CharField(default=b'O', max_length=1, null=True, choices=[(b'W', b'Waves'), (b'Q', b'Quark'), (b'S', b'Spree'), (b'Z', b'Zephyr'), (b'T', b'TEDx'), (b'O', b'Others')]),
        ),
    ]
