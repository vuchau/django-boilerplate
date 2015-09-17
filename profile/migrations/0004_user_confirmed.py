# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20150917_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
