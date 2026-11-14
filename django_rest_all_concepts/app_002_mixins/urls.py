from django.urls import path
from app_002_mixins.views import *

urlpatterns = [
    path('jsonresponse/', jsonResponseView.as_view(), name='jsonresponse'),
    path('mixindata/', showMixinData.as_view(), name='mixindata'),
    path('infotest/<int:id>/', infotest.as_view(), name='infotest'),
    path('showinfo/', showinfoTestList.as_view(), name='showinfo'),
    path('showinfowithmixin/', showinfoTestListWithMixin.as_view(), name='showinfowithmixin'),
    path('testInfoFormView/<int:id>/', testInfoFormView.as_view(), name='testInfoFormView'),
]