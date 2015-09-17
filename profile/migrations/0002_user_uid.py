# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


def ad_uid(apps, schema_editor):
    """We need to make the categories for the db"""

    User = apps.get_model("profile", "User")
    for user in User.objects.all():
        user.uid = uuid.uuid4()
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.UUIDField(null=True),
        ),
        migrations.RunPython(ad_uid, ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False),
        )
    ]
