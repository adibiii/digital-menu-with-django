from django.urls import path

from lorca.views import home, index

urlpatterns = [
    path('', index),
    path('home/<int:table_id>/', home, name='home')
]