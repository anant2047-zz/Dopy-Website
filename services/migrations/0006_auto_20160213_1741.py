# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20160213_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='home_slider',
        ),
        migrations.RemoveField(
            model_name='service',
            name='panelImages',
        ),
        migrations.RemoveField(
            model_name='service',
            name='storage',
        ),
        migrations.AddField(
            model_name='service',
            name='advert',
            field=models.FileField(upload_to='services/advertisements/vid/', null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='photo',
            field=models.FileField(default='DEFAULT', upload_to='services/photography/img/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='wed',
            field=models.FileField(blank=True, upload_to='services/weddings/img/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='fest_name',
            field=models.CharField(max_length=1, choices=[('P', 'Photography'), ('A', 'Advertisements'), ('W', 'Weddings')], default='P', null=True),
        ),
    ]
