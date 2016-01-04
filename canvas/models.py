from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


# Promo plugin model
class PromoPluginModel(CMSPlugin):

    background = models.ImageField(
        _('Background image'),
        blank=False,
        null=False,
        upload_to='upload/promo_box/',
        help_text=_('The background of the promo box')
    )
