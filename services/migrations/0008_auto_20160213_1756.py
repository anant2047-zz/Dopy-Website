# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20160213_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='advert',
            new_name='advertisement',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='photo',
            new_name='photograph',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='wed',
            new_name='wedding',
        ),
    ]
