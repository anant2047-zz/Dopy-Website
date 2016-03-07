# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0017_auto_20160215_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='link',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
    ]
