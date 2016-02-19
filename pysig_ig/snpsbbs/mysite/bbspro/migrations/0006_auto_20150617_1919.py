# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbspro', '0005_category_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='blockedperson',
            field=models.ManyToManyField(related_name='blockedperson', to='bbspro.BBS_User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='administrator',
            field=models.ForeignKey(related_name='administrator', to='bbspro.BBS_User'),
            preserve_default=True,
        ),
    ]
