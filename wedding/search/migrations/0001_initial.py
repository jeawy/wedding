# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('area', '0002_auto_20161221_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords', models.CharField(max_length=2048, null=True)),
                ('ip', models.CharField(max_length=48, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('area', models.ForeignKey(to='area.Area', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
