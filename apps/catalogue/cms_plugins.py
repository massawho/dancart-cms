from cms.cms_plugins import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import ProductListPluginModel, Product, Brand


class MostViewedProductsPlugin(CMSPluginBase):

    model = ProductListPluginModel
    module = _('Catalogue')
    name = _('Most viewed products')
    render_template = 'catalogue/cms_plugins/most_viewed_products.html'

    def render(self, context, instance, placeholder):
        products = Product.objects.most_popular()[:instance.num_items]
        context.update({'products': products})
        return context


class MostRecentProductsPlugin(CMSPluginBase):

    model = ProductListPluginModel
    module = _('Catalogue')
    name = _('Most recent products')
    render_template = 'catalogue/cms_plugins/most_recent_products.html'

    def render(self, context, instance, placeholder):
        products = Product.objects.added_recently()[:instance.num_items]
        context.update({'products': products})
        return context


class BrandListPlugin(CMSPluginBase):

    module = _('Catalogue')
    name = _('Brand List')
    render_template = 'catalogue/cms_plugins/brand_list.html'

    def render(self, context, instance, placeholder):
        brands = Brand.objects.all()
        context.update({'brands': brands})
        return context


plugin_pool.register_plugin(MostViewedProductsPlugin)
plugin_pool.register_plugin(MostRecentProductsPlugin)
plugin_pool.register_plugin(BrandListPlugin)