from django.conf.urls import patterns, url
from apps.catalogue.views import ProductDetail, set_visit

urlpatterns = patterns('',
   url(r'^(?P<slug>[a-z-0-9]+)/$', ProductDetail.as_view(), name="product_details"),
   url(r'^(?P<slug>[a-z-0-9]+)/set-visit/$', set_visit, name="product_set_visit"),
)
