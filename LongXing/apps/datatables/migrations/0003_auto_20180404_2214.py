# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-04 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datatables', '0002_auto_20180403_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasedatamodel',
            name='add_time',
        ),
        migrations.RemoveField(
            model_name='purchasedatamodel',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='purchasetablemodel',
            name='selldata',
        ),
        migrations.RemoveField(
            model_name='selldatamodel',
            name='add_time',
        ),
        migrations.RemoveField(
            model_name='selldatamodel',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='selltablemodel',
            name='selldata',
        ),
        migrations.AddField(
            model_name='purchasedatamodel',
            name='dataid',
            field=models.IntegerField(default=0, verbose_name='进货单id'),
        ),
        migrations.AddField(
            model_name='purchasedatamodel',
            name='purchasedata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datatables.PurchaseTableModel', verbose_name='售货数据'),
        ),
        migrations.AddField(
            model_name='purchasetablemodel',
            name='owner',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='货主'),
        ),
        migrations.AddField(
            model_name='selldatamodel',
            name='dataid',
            field=models.IntegerField(default=0, verbose_name='数据id'),
        ),
        migrations.AddField(
            model_name='selldatamodel',
            name='datatable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datatables.SellTableModel', verbose_name='售货单'),
        ),
        migrations.AddField(
            model_name='selltablemodel',
            name='customer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='客户名'),
        ),
    ]