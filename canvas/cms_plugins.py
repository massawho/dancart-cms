from cms.cms_plugins import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import PromoPluginModel, FancyTitlePluginModel


class PromoPlugin(CMSPluginBase):

    module = _('Canvas template')
    name = _('Promo box')
    model = PromoPluginModel
    allow_children = True
    render_template = 'canvas/cms_plugins/promo_plugin.html'

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


class FancyTitlePlugin(CMSPluginBase):

    module = _('Canvas template')
    name = _('Fancy title')
    model = FancyTitlePluginModel
    render_template = 'canvas/cms_plugins/title.html'

    def render(self, context, instance, placeholder):
        context['center'] = instance.center
        context['top_margin'] = instance.top_margin
        context['title'] = instance.title
        return context


plugin_pool.register_plugin(PromoPlugin)
plugin_pool.register_plugin(FancyTitlePlugin)