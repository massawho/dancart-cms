# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20151231_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visits',
            field=models.PositiveIntegerField(default=0, verbose_name='Number of visit', help_text='Number of times this product has been visited'),
        ),
    ]
