from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline
from .models import Product, Category, Photo, Brand
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(
        Category,
        exclude=('slug',)
    )


class PhotoInline(SortableTabularInline):
    model = Photo
    extra = 1
    fields = ['file', 'description']


class ProductAdmin(NonSortableParentAdmin):
    exclude = ('slug', 'visits')
    list_display = ('name', 'get_default_photo_thumbnail', 'price', 'brand')
    filter_horizontal = ('related_products', 'categories')
    inlines = [PhotoInline]
    fieldsets = (
        ('Basic info', {
            'fields': ('name', 'description', 'categories', 'price', 'discount_price', 'brand')
        }),
        (_('Related products'), {
            'fields': ('related_products', )
        })
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
