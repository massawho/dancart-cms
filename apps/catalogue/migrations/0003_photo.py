# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.catalogue.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20151017_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=60, verbose_name='Description')),
                ('item_order', models.PositiveIntegerField(default=0)),
                ('logo', sorl.thumbnail.fields.ImageField(upload_to=apps.catalogue.models.get_product_photo_path)),
                ('product', models.ForeignKey(to='catalogue.Product')),
            ],
            options={
                'ordering': ['item_order'],
            },
        ),
    ]
