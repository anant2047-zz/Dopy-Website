# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20160118_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('event_name', models.CharField(max_length=120)),
                ('upload_file', models.FileField(upload_to='Images/')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadImage',
        ),
    ]
