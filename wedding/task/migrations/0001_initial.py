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
            name='Todo_comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('conmments', models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
            ],
        ),
        migrations.CreateModel(
            name='Todo_engineer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('status', models.CharField(default=b'1', max_length=10)),
                ('reason', models.TextField(verbose_name=b'\xe6\x8b\x92\xe7\xbb\x9d\xe7\x9a\x84\xe5\x8e\x9f\xe5\x9b\xa0')),
                ('engineer', models.ForeignKey(verbose_name=b'\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xb8\x88', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Todo_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('description', models.TextField(verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('finish_date', models.DateTimeField(null=True, verbose_name=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\xae\x8c\xe6\x88\x90\xe7\x9a\x84\xe6\x97\xa5\xe6\x9c\x9f')),
                ('title', models.CharField(default=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0', max_length=1000, verbose_name=b'\xe5\xbe\x85\xe5\x8a\x9e\xe4\xbb\xbb\xe5\x8a\xa1')),
                ('status', models.CharField(default=b'0', max_length=10)),
                ('finisher', models.ForeignKey(related_name='finisher', verbose_name=b'finisher', to=settings.AUTH_USER_MODEL, null=True)),
                ('publisher', models.ForeignKey(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe8\x80\x85', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'permissions': (('manage_todolist', 'Can manage TODO list'),),
            },
        ),
        migrations.AddField(
            model_name='todo_engineer',
            name='todo_id',
            field=models.ForeignKey(to='task.Todo_list'),
        ),
        migrations.AddField(
            model_name='todo_comments',
            name='todo_id',
            field=models.ForeignKey(to='task.Todo_list'),
        ),
        migrations.AddField(
            model_name='todo_comments',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe5\xb7\xa5\xe7\xa8\x8b\xe5\xb8\x88', to=settings.AUTH_USER_MODEL),
        ),
    ]
