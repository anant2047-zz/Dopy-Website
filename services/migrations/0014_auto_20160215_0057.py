# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_auto_20160214_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='user',
        ),
        migrations.AddField(
            model_name='userinformation',
            name='email',
            field=models.EmailField(max_length=254, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinformation',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='address',
            field=models.CharField(max_length=100, default='fsf', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='contact_number',
            field=models.IntegerField(null=True),
        ),
    ]
