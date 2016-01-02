from django.conf.urls import patterns, url
from .views import ProductList, CategoryList, ProductDetail

urlpatterns = patterns('',
                       url(r'^(?P<category>[a-z-]+)/$', CategoryList.as_view(), name="category"),
                       url(r'^(?P<category>[a-z-]+)/(?P<slug>[a-z-]+)/$', ProductDetail.as_view(), name="product_details"),
                       url(r'$', ProductList.as_view(), name="all_products")
                       )