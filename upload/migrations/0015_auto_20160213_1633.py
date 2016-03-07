# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0014_auto_20160212_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='fest_name',
            field=models.CharField(choices=[('W', 'Waves'), ('Q', 'Quark'), ('S', 'Spree'), ('C', 'Coalescence'), ('T', 'TEDx'), ('O', 'Others')], null=True, max_length=1, default='O'),
        ),
    ]
