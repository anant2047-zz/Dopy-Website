# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20160213_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='advertisement',
            new_name='advertisements',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='wedding',
            new_name='weddings',
        ),
    ]
