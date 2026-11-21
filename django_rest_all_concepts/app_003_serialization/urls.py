from django.urls import path
from app_003_serialization.views import *

urlpatterns = [
    path('detailview', detailView.as_view(), name='detailview')
]