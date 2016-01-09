from django.conf.urls import patterns, url
from apps.catalogue.views import ProductList, CategoryList, ProductDetail, set_visit

urlpatterns = patterns('',
   url(r'^(?P<category>[a-z-/]+)/$', CategoryList.as_view(), name="category"),
   url(r'^(?P<category>[a-z-/]+)/(?P<slug>[a-z-]+)/set-visit/$', set_visit, name="product_set_visit"),
   url(r'$', ProductList.as_view(), name="all_products")
)