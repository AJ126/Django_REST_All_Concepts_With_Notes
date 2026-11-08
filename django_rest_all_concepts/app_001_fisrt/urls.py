from django.urls import path
from .views import *

urlpatterns = [
    path('first/', first_api, name='first_api'),
    path('customers/', customer_list, name='customer_list'),
]