# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0008_auto_20170212_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='kb_magazine',
            name='magazine',
            field=models.ForeignKey(default=1, to='kb.Magazine'),
            preserve_default=False,
        ),
    ]
