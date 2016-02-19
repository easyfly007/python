# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bbspro', '0004_tiezi_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 31, 8, 9, 29, 749000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
