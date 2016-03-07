# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0013_uploadfile_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='fest_name',
            field=models.CharField(null=True, max_length=1, default='O', choices=[('W', 'Waves'), ('Q', 'Quark'), ('S', 'Spree'), ('C', 'Coalescence'), ('T', 'TEDX'), ('O', 'Others')]),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='link',
            field=models.CharField(max_length=240, blank=True),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='storage',
            field=models.FileField(null=True, upload_to='temporary/storage/'),
        ),
    ]
