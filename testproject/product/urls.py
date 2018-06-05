from django.conf.urls import url
from product.views import ProductListView, ProductDetailView

app_name = 'product'

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
]