# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0017_auto_20160213_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='LostAndFound',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('link', models.CharField(blank=True, max_length=240, default='notfound')),
                ('year', models.CharField(max_length=4, null=True)),
                ('event_name', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='link',
            field=models.CharField(blank=True, max_length=240, default='Paste Here....'),
        ),
    ]
