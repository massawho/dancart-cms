# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('catalogue', '0008_auto_20160101_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductListPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, to='cms.CMSPlugin', auto_created=True, parent_link=True)),
                ('num_items', models.PositiveIntegerField(help_text='Number of items to be displayed', verbose_name='Number of items')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
