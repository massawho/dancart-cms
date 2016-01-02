# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='related_products',
            field=models.ManyToManyField(blank=True, help_text='Products that are related to this product.', to='catalogue.Product', verbose_name='List of products.', related_name='_related_products_+'),
        ),
    ]
