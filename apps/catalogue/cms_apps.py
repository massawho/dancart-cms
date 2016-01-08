from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .menu import CategoryMenu


class CatalogueApp(CMSApp):
    name = _("Catalogue")
    urls = ["apps.catalogue.urls.catalogue"]
    menus = [CategoryMenu]


class ProductApp(CMSApp):
    name = _("Product details")
    urls = ["apps.catalogue.urls.product"]

apphook_pool.register(CatalogueApp)
apphook_pool.register(ProductApp)
