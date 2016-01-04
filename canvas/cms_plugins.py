from cms.cms_plugins import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from apps.catalogue.models import Product
from .models import PromoPluginModel


class PromoPlugin(CMSPluginBase):

    module = _('Canvas template')
    name = _('Promo box')
    model = PromoPluginModel
    allow_children = True
    render_template = 'canvas/cms_plugins/promo_plugin.html'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(PromoPlugin)