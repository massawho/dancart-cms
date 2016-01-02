# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.catalogue.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20151018_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80, verbose_name='Brand name')),
                ('logo', sorl.thumbnail.fields.ImageField(help_text='Logo of this brand', verbose_name='Logo', upload_to=apps.catalogue.models.get_brand_logo_path)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(to='catalogue.Brand', null=True),
        ),
    ]
