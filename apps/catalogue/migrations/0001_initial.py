# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=45)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Product name')),
                ('description', models.TextField(verbose_name='Product description')),
                ('publication_date', models.DateField(auto_now_add=True, help_text='Date when this product was published.', verbose_name='Publication date')),
                ('price', models.DecimalField(blank=True, max_digits=8, null=True, decimal_places=2)),
                ('discount_price', models.DecimalField(blank=True, max_digits=8, null=True, decimal_places=2)),
                ('slug', models.SlugField(max_length=140, help_text='A unique name to identify this product.', verbose_name='Slug')),
                ('category', models.ForeignKey(help_text='Category of this product', to='catalogue.Category')),
                ('related_products', models.ManyToManyField(related_name='_related_products_+', help_text='Products that are related to this product.', to='catalogue.Product', verbose_name='List of products.')),
            ],
        ),
    ]
