# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0002_auto_20160124_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fancytitlepluginmodel',
            name='title',
            field=models.CharField(help_text='Title to be displayed', verbose_name='Title', max_length=60),
        ),
    ]
