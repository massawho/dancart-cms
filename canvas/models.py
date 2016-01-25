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


# Fancy title plugin model
class FancyTitlePluginModel(CMSPlugin):

    MARGIN_TOP = (
        ('', 'None'),
        ('sm', 'Small'),
        ('md', 'Medium'),
        ('lg', 'Large')
    )

    title = models.CharField(
        _('Title'),
        max_length=60,
        blank=False,
        null=False,
        help_text=_('Title to be displayed')
    )

    top_margin = models.CharField(
        _('Margin top'),
        max_length=20,
        blank=True,
        null=False,
        choices=MARGIN_TOP,
        default='',
        help_text=_('Size of the margin top')
    )

    center = models.BooleanField(
        _('Centered'),
        max_length=20,
        default=False,
        help_text=_('Should the title be centered?')
    )

    def __str__(self):
        return self.title