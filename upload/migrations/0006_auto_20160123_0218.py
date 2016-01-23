# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20160122_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='panelImages',
            field=models.FileField(upload_to='events/panelImages/'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='sliderImages',
            field=models.FileField(upload_to='events/sliderImages/'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='storage',
            field=models.FileField(upload_to='events/storage/'),
        ),
    ]
