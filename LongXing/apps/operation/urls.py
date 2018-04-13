# _*_ coding:utf-8 _*_
from django.conf.urls import url

from .views import SellView

urlpatterns = [
    url(r'^sell$', SellView.as_view(), name='operation_sell'),
]