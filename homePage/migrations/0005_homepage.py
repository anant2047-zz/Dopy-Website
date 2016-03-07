# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0004_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sliderImages', models.FileField(blank=True, null=True, upload_to='homeslider/slider/img')),
                ('thumbnails', models.FileField(blank=True, null=True, upload_to='homeslider/slider/thumbnails')),
            ],
        ),
    ]
