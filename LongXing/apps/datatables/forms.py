# _*_ coding:utf-8 _*_
from django import forms
from .models import SelldataModel

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = SelldataModel
        fields = ['author','title','detail','image']
