__author__ = 'massa'

from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from .models import Category


class CategoryMenu(CMSAttachMenu):

    name = _("Category Menu")
    template = "category_menu.html"

    def get_nodes(self, request):
        nodes = []
        for category in Category.objects.all():

            parent = category.get_parent()

            if parent is not None:
                parent = parent.slug

            node = NavigationNode(
                category.name,
                category.get_absolute_url(),
                category.slug,
                parent
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(CategoryMenu)