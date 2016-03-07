# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0005_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='sliderImages',
            field=models.FileField(upload_to='temporary/panelImages/', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='thumbnails',
            field=models.FileField(upload_to='temporary/thumbnails/', blank=True, null=True),
        ),
    ]
