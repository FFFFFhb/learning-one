# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-03 11:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datatables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebtModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('who', models.CharField(max_length=50, verbose_name='主导人')),
                ('money', models.IntegerField(default=0, verbose_name='金额')),
            ],
            options={
                'verbose_name': '欠款单',
                'verbose_name_plural': '欠款单',
            },
        ),
        migrations.CreateModel(
            name='ImportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('customer', models.CharField(max_length=50, verbose_name='客户名')),
                ('money', models.IntegerField(default=0, verbose_name='金额')),
            ],
            options={
                'verbose_name': '汇入单',
                'verbose_name_plural': '汇入单',
            },
        ),
        migrations.CreateModel(
            name='PurchasedataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('owner', models.CharField(max_length=50, verbose_name='货主')),
                ('size', models.CharField(blank=True, max_length=10, null=True, verbose_name='规格')),
                ('amount', models.IntegerField(default=0, verbose_name='件数')),
                ('kilo', models.IntegerField(default=0, verbose_name='斤数')),
                ('price', models.IntegerField(default=0, verbose_name='价格')),
                ('totalprice', models.IntegerField(default=0, verbose_name='金额')),
            ],
            options={
                'verbose_name': '进货单数据',
                'verbose_name_plural': '进货单数据',
            },
        ),
        migrations.CreateModel(
            name='PurchaseTableModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField(default=0, verbose_name='总件数')),
                ('total_kilos', models.IntegerField(default=0, verbose_name='总斤数')),
                ('total_price', models.IntegerField(default=0, verbose_name='总金额')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('selldata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datatables.PurchasedataModel', verbose_name='售货数据')),
            ],
            options={
                'verbose_name': '进货单',
                'verbose_name_plural': '进货单',
            },
        ),
        migrations.CreateModel(
            name='RemittanceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('customer', models.CharField(max_length=50, verbose_name='客户名')),
                ('money', models.IntegerField(default=0, verbose_name='金额')),
            ],
            options={
                'verbose_name': '汇出单',
                'verbose_name_plural': '汇出单',
            },
        ),
        migrations.CreateModel(
            name='SpendingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('content', models.CharField(max_length=100, verbose_name='内容')),
                ('who', models.CharField(max_length=50, verbose_name='主导人')),
                ('money', models.IntegerField(default=0, verbose_name='金额')),
            ],
            options={
                'verbose_name': '开支表',
                'verbose_name_plural': '开支表',
            },
        ),
        migrations.RemoveField(
            model_name='selldatamodel',
            name='score',
        ),
    ]
