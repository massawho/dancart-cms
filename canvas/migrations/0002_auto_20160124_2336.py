# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fancytitlepluginmodel',
            name='margin_top',
        ),
        migrations.AddField(
            model_name='fancytitlepluginmodel',
            name='top_margin',
            field=models.CharField(max_length=20, choices=[('', 'None'), ('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')], help_text='Size of the margin top', default='', verbose_name='Margin top'),
        ),
    ]
