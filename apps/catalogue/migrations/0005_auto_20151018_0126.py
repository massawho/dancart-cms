# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20151018_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='logo',
            new_name='file',
        ),
    ]
