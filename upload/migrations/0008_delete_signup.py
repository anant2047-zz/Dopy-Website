# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_uploadfile_thumbnails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
