# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(to='catalogue.Product', related_name='_related_products_+', blank=True, help_text='Products that are related to this product.', verbose_name='List of related products'),
        ),
    ]
