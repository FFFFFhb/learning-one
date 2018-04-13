# _*_ coding:utf-8 _*_
from django.conf.urls import url

from .views import SelllistView,addSellView,addDangkoukaizhiView,addDebtView,addHuichuView,addHuiruView,addJinhuoView
from .views import PurchaselistView,SpendinglistView,HuichulistView,HuirulistView,QiandanlistView

urlpatterns = [
    url(r'^selllist$', SelllistView.as_view(), name='datatables_selllist'),
    url(r'^purchaselist$', PurchaselistView.as_view(), name='datatables_purchaselist'),
    url(r'^spendinglist$', SpendinglistView.as_view(), name='datatables_spendinglist'),
    url(r'^huichulist$', HuichulistView.as_view(), name='datatables_huichulist'),
    url(r'^huirulist$', HuirulistView.as_view(), name='datatables_huirulist'),
    url(r'^qiandanlist$', QiandanlistView.as_view(), name='datatables_qiandanlist'),


    url(r'^addsell$',addSellView.as_view(),name='datatables_addsell'),
    url(r'^adddangkoukaizhi$',addDangkoukaizhiView.as_view(),name='datatables_adddangkoukaizhi'),
    url(r'^adddebt$',addDebtView.as_view(),name='datatables_adddebt'),
    url(r'^addhuichu$',addHuichuView.as_view(),name='datatables_addhuichu'),
    url(r'^addhuiru$',addHuiruView.as_view(),name='datatables_addhuiru'),
    url(r'^addjinhuo$',addJinhuoView.as_view(),name='datatables_addjinhuo'),
]