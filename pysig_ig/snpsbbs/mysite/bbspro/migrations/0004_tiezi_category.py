# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbspro', '0003_remove_tiezi_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiezi',
            name='category',
            field=models.ForeignKey(default=1, to='bbspro.Category'),
            preserve_default=False,
        ),
    ]
