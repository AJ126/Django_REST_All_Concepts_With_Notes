from django.urls import path
from app_004_modelSerialization.views import *

urlpatterns = [
    path('infoapi', informationView.as_view(), name='infoapi')
]
