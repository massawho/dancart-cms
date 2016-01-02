from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .menu import CategoryMenu

class CatalogueApp(CMSApp):
    name = _("Catalogue")
    urls = ["apps.catalogue.urls"]
    menus = [CategoryMenu]

apphook_pool.register(CatalogueApp)