# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20160215_0057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinformation',
            old_name='email',
            new_name='user_email',
        ),
    ]
