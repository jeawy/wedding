# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=b'/', max_length=2048)),
                ('piclink', models.CharField(max_length=2048, null=True)),
                ('msgtext', models.CharField(default=b'new msg', max_length=2048)),
                ('visibility', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
