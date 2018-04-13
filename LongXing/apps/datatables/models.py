from django.db import models
from datetime import datetime

# Create your models here.

class SellTableModel(models.Model):
    customer = models.CharField(max_length=50, verbose_name=u'客户名', null=True, blank=True)
    total_kilos = models.IntegerField(default=0,verbose_name=u'总斤数')
    total_price = models.IntegerField(default=0,verbose_name=u'总金额')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'售货单'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.customer

class SelldataModel(models.Model):
    datatable = models.ForeignKey(SellTableModel,verbose_name=u'售货单', null=True, blank=True)
    dataid = models.IntegerField(default=0,verbose_name=u'数据id')
    size = models.CharField(max_length=10, verbose_name=u'规格', null=True, blank=True)
    kilo = models.IntegerField(default=0, verbose_name=u'斤数')
    price = models.IntegerField(default=0, verbose_name=u'价格')
    totalprice =models.IntegerField(default=0, verbose_name=u'金额')
    debts = models.CharField(max_length=10, verbose_name=u'是否欠账')

    class Meta:
        verbose_name = u'售货单数据'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.dataid



class PurchaseTableModel(models.Model):

    owner = models.CharField(max_length=50, verbose_name=u'货主', null=True, blank=True)
    total_amount = models.IntegerField(default=0,verbose_name=u'总件数')
    total_kilos = models.IntegerField(default=0,verbose_name=u'总斤数')
    total_price = models.IntegerField(default=0,verbose_name=u'总金额')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'进货单'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.add_time

class PurchasedataModel(models.Model):
    purchasedata = models.ForeignKey(PurchaseTableModel, verbose_name=u'售货数据', null=True, blank=True)
    dataid = models.IntegerField(default=0,verbose_name=u'进货单id')
    size = models.CharField(max_length=10, verbose_name=u'规格', null=True, blank=True)
    amount = models.IntegerField(default=0,verbose_name=u'件数')
    kilo = models.IntegerField(default=0, verbose_name=u'斤数')
    price = models.IntegerField(default=0, verbose_name=u'价格')
    totalprice =models.IntegerField(default=0, verbose_name=u'金额')

    class Meta:
        verbose_name = u'进货单数据'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.dataid

class RemittanceModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    customer = models.CharField(max_length=50,verbose_name=u'客户名')
    money = models.IntegerField(default=0,verbose_name=u'金额')

    class Meta:
        verbose_name = u'汇出单'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.customer

class ImportModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    customer = models.CharField(max_length=50,verbose_name=u'客户名')
    money = models.IntegerField(default=0,verbose_name=u'金额')

    class Meta:
        verbose_name = u'汇入单'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.customer

class SpendingModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    content = models.CharField(max_length=100,verbose_name=u'内容')
    who = models.CharField(max_length=50, verbose_name=u'主导人')
    money = models.IntegerField(default=0, verbose_name=u'金额')

    class Meta:
        verbose_name = u'开支表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.who


class DebtModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    who = models.CharField(max_length=50, verbose_name=u'主导人')
    money = models.IntegerField(default=0, verbose_name=u'金额')

    class Meta:
        verbose_name = u'欠款单'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.who