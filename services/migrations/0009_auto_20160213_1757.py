# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20160213_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='photograph',
            new_name='photography',
        ),
    ]
