# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20160213_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='advertisements',
        ),
        migrations.RemoveField(
            model_name='service',
            name='photography',
        ),
        migrations.RemoveField(
            model_name='service',
            name='weddings',
        ),
        migrations.AddField(
            model_name='service',
            name='panelImages',
            field=models.FileField(upload_to='temporary/services/panelImages/', null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='thumbnails',
            field=models.FileField(upload_to='temporary/services/thumbnails/', null=True),
        ),
    ]
