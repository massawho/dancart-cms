from django.conf.urls import patterns, url
from apps.catalogue.views import ProductList, CategoryList, ProductDetail, set_visit

urlpatterns = patterns('',
   url(r'^(?P<slug>[a-z-]+)/$', ProductDetail.as_view(), name="product_details"),
   url(r'^(?P<slug>[a-z-]+)/set-visit/$', set_visit, name="product_set_visit"),
)