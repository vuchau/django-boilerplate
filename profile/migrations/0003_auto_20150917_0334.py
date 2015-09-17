# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_user_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_password_requested',
            field=models.BooleanField(default=False),
        ),
    ]
