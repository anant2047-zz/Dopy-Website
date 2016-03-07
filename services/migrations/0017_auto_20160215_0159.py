# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_auto_20160215_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='full_name',
            field=models.CharField(null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='user_email',
            field=models.EmailField(default='email', max_length=254),
            preserve_default=False,
        ),
    ]
