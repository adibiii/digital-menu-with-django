from django.urls import path

from basket.views import add, orders_list

urlpatterns = [
    path('add/<int:table_id>', add, name='add'),
    path('orders/<int:table_id>', orders_list, name='orders')
]
