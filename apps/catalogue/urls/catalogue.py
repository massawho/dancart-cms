from django.conf.urls import patterns, url
from apps.catalogue.views import ProductList, CategoryList

urlpatterns = patterns('',
   url(r'^(?P<category>[a-z-0-9/]+)/$', CategoryList.as_view(), name="category"),
   url(r'$', ProductList.as_view(), name="all_products")
)
