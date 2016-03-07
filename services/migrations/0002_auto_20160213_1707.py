# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('photography', models.FileField(blank=True, upload_to='services/photography', null=True)),
                ('advertisements', models.FileField(blank=True, upload_to='services/advertisements/vid', null=True)),
                ('weddings', models.FileField(blank=True, upload_to='services/weddings/img', null=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('service_name', models.CharField(default='O', max_length=1, null=True, choices=[('P', 'Photography'), ('A', 'Advertisements'), ('W', 'Weddings')])),
            ],
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
