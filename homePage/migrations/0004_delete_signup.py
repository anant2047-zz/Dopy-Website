# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_auto_20160123_1630'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
