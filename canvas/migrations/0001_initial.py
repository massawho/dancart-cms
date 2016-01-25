# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='FancyTitlePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', parent_link=True, auto_created=True, serialize=False)),
                ('title', models.CharField(help_text='Title to be displayed', max_length=20, verbose_name='Title')),
                ('margin_top', models.CharField(help_text='Title to be displayed', choices=[('', 'None'), ('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')], default='', verbose_name='Title', max_length=20)),
                ('center', models.BooleanField(verbose_name='Centered', help_text='Should the title be centered?', max_length=20, default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PromoPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, to='cms.CMSPlugin', parent_link=True, auto_created=True, serialize=False)),
                ('background', models.ImageField(help_text='The background of the promo box', upload_to='upload/promo_box/', verbose_name='Background image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
