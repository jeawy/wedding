# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': (('cannot_publish_kb', '\u9ed1\u540d\u5355:\u4e0d\u80fd\u53d1\u5e16\uff0c\u4e0d\u80fd\u56de\u5e16'), ('cannot_modify_kb', '\u4fee\u6539\u5e16\u5b50\u6743\u9650:\u6ca1\u6709\u6743\u9650\u4fee\u6539\u5e16\u5b50'), ('can_modify_all_kb_top_pic', '\u53ef\u4ee5\u8bbe\u7f6e\u6240\u6709\u5e16\u5b50\u7684\u9876\u56fe'), ('can_modify_all_kb', '\u7ba1\u7406\u5458\u53ef\u4ee5\u4fee\u6539\u6240\u6709\u4eba\u7684\u8d34\u5b50'), ('can_del_all_kb', '\u7ba1\u7406\u5458\u53ef\u4ee5\u5220\u9664\u6240\u6709\u4eba\u7684\u8d34\u5b50'), ('manage_all_kb', '\u7ba1\u7406\u8d34\u5b50\uff1a\u5220\u9664\uff0c\u8bbe\u4e3a\u7cbe\u534e\uff0c\u8bbe\u7f6e\u8f6e\u64ad\u56fe.'), ('check_kb_autor', '\u6709\u67e5\u770b\u5e16\u5b50\u4f5c\u8005\u540d\u79f0.'))},
        ),
    ]
