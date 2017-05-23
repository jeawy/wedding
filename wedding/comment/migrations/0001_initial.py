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
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('type', models.IntegerField(default=0)),
                ('commenter', models.ForeignKey(related_name='commenter', verbose_name=b'', to=settings.AUTH_USER_MODEL)),
                ('replied_comment', models.ForeignKey(to='comment.Comment', null=True)),
            ],
            options={
                'permissions': (('forbid_comment', 'forbid an User to comment any feature'),),
            },
        ),
    ]
