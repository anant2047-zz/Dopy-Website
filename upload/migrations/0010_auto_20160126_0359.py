# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_uploadfile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='home_slider',
            field=models.FileField(upload_to='home_slider', blank=True),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='panelImages',
            field=models.FileField(upload_to='temporary/panelImages/'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='sliderImages',
            field=models.FileField(upload_to='temporary/sliderImages/'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='storage',
            field=models.FileField(upload_to='temporary/storage/'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='thumbnails',
            field=models.FileField(upload_to='temporary/thumbnails', blank=True),
        ),
    ]
