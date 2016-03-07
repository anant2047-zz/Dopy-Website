# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0011_auto_20160214_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('contact_number', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='panelImages',
            field=models.FileField(null=True, upload_to='temporary/panelImages/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='thumbnails',
            field=models.FileField(null=True, upload_to='temporary/thumbnails/'),
        ),
    ]
