from django.urls import path

from products.views import *
from django.views.decorators.cache import cache_page

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('charx/', CharView.as_view(), name='char'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),

]

