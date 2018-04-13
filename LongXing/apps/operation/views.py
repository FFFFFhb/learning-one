# _*_ coding:utf-8 _*_
import datetime
import json

from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class SellView(View):
    def get(self,request):
        return render(request,'shouhuo.html',{})