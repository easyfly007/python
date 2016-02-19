# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('case', models.CharField(default=b'', max_length=100)),
                ('caselist', models.CharField(default=b'', max_length=10)),
                ('rundate', models.CharField(default=b'', max_length=8)),
                ('trandiff', models.FloatField()),
                ('comparenote', models.CharField(default=b'', max_length=10)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
    ]
