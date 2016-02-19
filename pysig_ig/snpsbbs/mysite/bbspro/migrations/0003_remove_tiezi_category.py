# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbspro', '0002_auto_20150503_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiezi',
            name='category',
        ),
    ]
