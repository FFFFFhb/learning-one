from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u'昵称',default='',null=True,blank=True)
    birthday = models.DateTimeField(verbose_name=u'生日',null=True,blank=True)
    gender = models.CharField(choices=(('male',u'男'),('female',u'女')),default='female',max_length=7)
    mobile = models.CharField(max_length=11,null=True,blank=True)
    address = models.CharField(max_length=150, default=u'',null=True,blank=True)
    is_org = models.CharField(choices=(('yes',u'是'),('no',u'否')),default='no',max_length=7)
    add_time = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username