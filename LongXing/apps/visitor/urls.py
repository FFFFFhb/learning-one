# _*_ coding:utf-8 _*_
from django.conf.urls import url

from .views import homeView

urlpatterns = [
    url(r'^home', homeView.as_view(), name='visitor_home'),
]