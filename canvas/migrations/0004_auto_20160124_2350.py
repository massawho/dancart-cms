# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0003_auto_20160124_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fancytitlepluginmodel',
            name='top_margin',
            field=models.CharField(max_length=20, default='', blank=True, choices=[('', 'None'), ('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')], verbose_name='Margin top', help_text='Size of the margin top'),
        ),
    ]
