# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20160213_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='fest_name',
            new_name='service_name',
        ),
    ]
