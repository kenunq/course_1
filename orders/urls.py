from django.urls import path

from orders.views import *
from django.views.decorators.cache import cache_page

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order-create'),

]

