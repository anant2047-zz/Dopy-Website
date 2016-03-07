# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_service_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='panelImages',
            field=models.FileField(blank=True, null=True, upload_to='temporary/panelImages/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='thumbnails',
            field=models.FileField(blank=True, null=True, upload_to='temporary/thumbnails/'),
        ),
    ]
