# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('service_name', models.CharField(choices=[('P', 'Photography'), ('A', 'Advertisements'), ('W', 'Weddings')], null=True, max_length=1, default='O')),
                ('photography', models.FileField(blank=True, null=True, upload_to='services/photography')),
                ('advertisements', models.FileField(blank=True, null=True, upload_to='services/advertisements/vid')),
                ('weddings', models.FileField(blank=True, null=True, upload_to='services/weddings/img')),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
