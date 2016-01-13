from adminsortable.admin import NonSortableParentAdmin, SortableTabularInline
from .models import Product, Category, Photo, Brand
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
    filter_horizontal = ('related_products', 'categories')
    inlines = [PhotoInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
