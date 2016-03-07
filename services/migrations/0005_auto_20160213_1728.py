# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20160213_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('panelImages', models.FileField(upload_to='temporary/panelImages/')),
                ('storage', models.FileField(null=True, upload_to='temporary/storage/')),
                ('home_slider', models.FileField(upload_to='home_slider', blank=True)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('fest_name', models.CharField(max_length=1, null=True, default='O', choices=[('W', 'Waves'), ('Q', 'Quark'), ('S', 'Spree')])),
            ],
        ),
        migrations.DeleteModel(
            name='UploadFile',
        ),
    ]
