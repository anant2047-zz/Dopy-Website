# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20160213_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('event_name', models.CharField(max_length=120)),
                ('sliderImages', models.FileField(upload_to='temporary/sliderImages/')),
                ('panelImages', models.FileField(upload_to='temporary/panelImages/')),
                ('storage', models.FileField(upload_to='temporary/storage/', null=True)),
                ('link', models.CharField(blank=True, default='NOT FOUND', max_length=240)),
                ('thumbnails', models.FileField(blank=True, upload_to='temporary/thumbnails')),
                ('home_slider', models.FileField(blank=True, upload_to='home_slider')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('year', models.CharField(null=True, max_length=4)),
                ('fest_name', models.CharField(choices=[('W', 'Waves'), ('Q', 'Quark'), ('S', 'Spree'), ('C', 'Coalescence'), ('T', 'TEDx'), ('O', 'Others')], default='O', null=True, max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
