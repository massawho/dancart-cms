from django.core.files.storage import get_storage_class
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from cms.cms_plugins import CMSPlugin
from sorl.thumbnail.shortcuts import get_thumbnail
from treebeard.mp_tree import MP_Node
from sorl.thumbnail import ImageField
from adminsortable.models import SortableMixin
import os


def get_brand_logo_path(instance, filename):
    return os.path.join("uploads/brands/", instance.name + instance.file_extension)


def get_product_photo_path(instance, filename):
    return os.path.join("uploads/products/%d" % instance.product.id, filename)


# Category class
class Category(MP_Node):

    class Meta:
        verbose_name_plural = _("categories")

    name = models.CharField(max_length=45)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.is_root():
            slug_list = set(slugify(ancestor.slug) for ancestor in self.get_ancestors())
            self.slug = '/'.join(slug_list) + "/%s" % slugify(self.name)
        else:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("category", args=[self.slug])

    def __str__(self):
        name_list = list(ancestor.name for ancestor in self.get_ancestors()) + [self.name]
        return ' / '.join(name_list)


# Brand class
class Brand(models.Model):

    name = models.CharField(
        _('Brand name'),
        max_length=80,
        null=False,
        blank=False
    )

    logo = ImageField(
        _('Logo'),
        upload_to=get_brand_logo_path,
        null=False,
        help_text=_('Logo of this brand')
    )

    def __str__(self):
        return self.name


# Product manager
class ProductManager(models.Manager):

    def most_popular(self):
        return self.order_by('-visits')

    def added_recently(self):
        return self.order_by('-publication_date')


# Product class
class Product(models.Model):

    objects = ProductManager()

    categories = models.ManyToManyField(
            Category,
            verbose_name=_('List of categories'),
            help_text=_('Categories of this product')
    )

    name = models.CharField(
            _('Product name'),
            max_length=140,
            null=False,
            blank=False
    )

    description = models.TextField(
            _('Product description'),
            null=False,
            blank=False
    )

    publication_date = models.DateField(
            _('Publication date'),
            null=False,
            blank=False,
            auto_now_add=True,
            help_text=_('Date when this product was published.')
    )

    visits = models.PositiveIntegerField(
            _('Number of visit'),
            default=0,
            null=False,
            blank=False,
            help_text=_('Number of times this product has been visited')
    )

    price = models.DecimalField(
            null=True,
            blank=True,
            max_digits=8,
            decimal_places=2
    )

    discount_price = models.DecimalField(
            null=True,
            blank=True,
            max_digits=8,
            decimal_places=2
    )

    slug = models.SlugField(
            _('Slug'),
            max_length=140,
            null=False,
            blank=False,
            help_text=_('A unique name to identify this product.')
    )

    related_products = models.ManyToManyField(
            'self',
            blank=True,
            verbose_name=_('List of related products'),
            help_text=_('Products that are related to this product.')
    )

    brand = models.ForeignKey(
            Brand,
            null=True,
            blank=True
    )

    def get_default_photo(self):
        if not hasattr(self, '__default_photo'):
            self.__default_photo = self.photo_set.first()
        return self.__default_photo

    def get_absolute_url(self):
        return reverse("product_details", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_no_photo_image(self):
        static_storage = get_storage_class(settings.STATICFILES_STORAGE)()
        return static_storage.url('images/no-image.png')

    def get_default_photo_thumbnail(obj):
        default_photo = obj.get_default_photo()
        url = get_thumbnail(
                default_photo.file,
                '100x100', crop='center', quality=99).url if default_photo is not None else obj.get_no_photo_image()
        return mark_safe("<img width=\"100px\" height=\"auto\" src=\"%s\">" %url)
    get_default_photo_thumbnail.short_description = _('')

    def __str__(self):
        return self.name

#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date < now
#
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'


class Photo(SortableMixin):

    class Meta:
        ordering = ['item_order']

    product = models.ForeignKey(Product)

    description = models.CharField(
        _('Description'),
        max_length=60
    )

    item_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False
    )

    file = ImageField(
        upload_to=get_product_photo_path,
        null=False
    )

    def __str__(self):
        return ''


""" ''''''''''''''''''''''''''''''

    SIGNALS

""" ''''''''''''''''''''''''''''''


@receiver(post_save, sender=Category, dispatch_uid='fix_category_children_slug')
def update_stock(sender, instance, **kwargs):
    for child in instance.get_children():
        child.save()


""" ''''''''''''''''''''''''''''''

    CMS PLUGIN MODELS

""" ''''''''''''''''''''''''''''''


# Product listing plugin model
class ProductListPluginModel(CMSPlugin):

    num_items = models.PositiveIntegerField(
        _('Number of items'),
        help_text='Number of items to be displayed'
    )
