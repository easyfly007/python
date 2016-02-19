# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbspro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiezi',
            name='category',
            field=models.ForeignKey(default=1, to='bbspro.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tiezi',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tiezi',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
