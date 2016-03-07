# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0015_auto_20160215_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='userinformation',
            name='user_email',
        ),
    ]
