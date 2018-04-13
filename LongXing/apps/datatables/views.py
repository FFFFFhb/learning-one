# _*_ coding:utf-8 _*_
from datetime import datetime
import json

from django.shortcuts import render
from django.views.generic import View

from .models import SellTableModel,SelldataModel,PurchaseTableModel,PurchasedataModel,RemittanceModel
from .models import DebtModel,ImportModel,SpendingModel

# Create your views here.
class SelllistView(View):
    def get(self,request):
        all_sell = SelldataModel.objects.all()
        count_sell = all_sell.count()
        total_kilo = 0
        total_price = 0
        for i in all_sell:
            total_kilo += i.kilo
            total_price += i.totalprice
        return render(request,'list-shouhuo.html',{
            'all_sell':all_sell,
            'count_sell':count_sell,
            'total_kilo':total_kilo,
            'total_price':total_price,
        })

class PurchaselistView(View):
    def get(self,request):
        all_purchase = PurchasedataModel.objects.all()
        count_purchase = all_purchase.count()
        total_kilo = 0
        total_price = 0
        total_number = 0
        for i in all_purchase:
            total_kilo += i.kilo
            total_price += i.totalprice
            total_number += i.amount
        return render(request,'list-jinhuo.html',{
            'all_purchase':all_purchase,
            'count_purchase':count_purchase,
            'total_kilo':total_kilo,
            'total_price':total_price,
            'total_number':total_number,
        })

class SpendinglistView(View):
    def get(self,request):
        all_spending = SpendingModel.objects.all()
        count_purchase = all_spending.count()
        total_money = 0
        for i in all_spending:
            total_money += i.money
        return render(request,'list-dangkoukaizhi.html',{
            'all_spending':all_spending,
            'count_purchase':count_purchase,
            'total_money':total_money,
        })

class HuichulistView(View):
    def get(self,request):
        all_huichu = RemittanceModel.objects.all()
        count_huichu = all_huichu.count()
        total_money = 0
        for i in all_huichu:
            total_money += i.money
        return render(request,'list-huichu.html',{
            'all_huichu': all_huichu,
            'count_huichu': count_huichu,
            'total_money': total_money,
        })

class HuirulistView(View):
    def get(self,request):
        all_huiru = ImportModel.objects.all()
        count_huiru = all_huiru.count()
        total_money = 0
        for i in all_huiru:
            total_money += i.money
        return render(request,'list-huiru.html',{
            'all_huiru': all_huiru,
            'count_huiru': count_huiru,
            'total_money': total_money,
        })

class QiandanlistView(View):
    def get(self,request):
        all_debt = DebtModel.objects.all()
        count_debt = all_debt.count()
        total_money = 0
        for i in all_debt:
            total_money += i.money
        return render(request,'list-qiandan.html',{
            'all_debt': all_debt,
            'count_debt': count_debt,
            'total_money': total_money,
        })

class addSellView(View):
    def get(self,request):
        return render(request,'shouhuo.html',{
        })
    def post(self,request):
        sell_data = request.POST
        if sell_data['date']:
            selldate = sell_data['date']
        else:
            selldate = datetime.now()
        sellcustomer = sell_data['customer']

        size1 = sell_data['size1']
        kilo1 = int(sell_data['kilo1'])
        price1 = int(sell_data['price1'])
        totalprice1 = int(kilo1 * price1)
        isdebt1 = sell_data['isdebt1']

        size2 = sell_data['size2']
        kilo2 = int(sell_data['kilo2'])
        price2 = int(sell_data['price2'])
        totalprice2 = int(kilo2 * price2)
        isdebt2 = sell_data['isdebt2']

        size3 = sell_data['size3']
        kilo3 = int(sell_data['kilo3'])
        price3 = int(sell_data['price3'])
        totalprice3 = int(kilo3 * price3)
        isdebt3 = sell_data['isdebt3']

        size4 = sell_data['size4']
        kilo4 = int(sell_data['kilo4'])
        price4 = int(sell_data['price4'])
        totalprice4 = int(kilo4 * price4)
        isdebt4 = sell_data['isdebt4']

        size5 = sell_data['size5']
        kilo5 = int(sell_data['kilo5'])
        price5 = int(sell_data['price5'])
        totalprice5 = int(kilo5 * price5)
        isdebt5 = sell_data['isdebt5']

        total_kilos = kilo1 + kilo2 + kilo3 + kilo4 + kilo5
        total_price = totalprice1 + totalprice2 + totalprice3 + totalprice4 + totalprice5

        def saveData(dataid, size, kilo, price, totalprice, isdebt):
            new_sell_data = SelldataModel()
            new_sell_data.datatable = new_sell_table
            new_sell_data.dataid = dataid
            new_sell_data.size = size
            new_sell_data.kilo = kilo
            new_sell_data.price = price
            new_sell_data.totalprice = totalprice
            new_sell_data.debts = isdebt
            new_sell_data.save()

        if sellcustomer and total_kilos and total_price:
            new_sell_table = SellTableModel()
            new_sell_table.customer = sellcustomer
            new_sell_table.total_kilos = total_kilos
            new_sell_table.total_price = total_price
            new_sell_table.add_time = selldate
            new_sell_table.save()
            if size1 and kilo1 and price1 and totalprice1 and isdebt1:
                saveData(1, size1, kilo1, price1, totalprice1, isdebt1)
            if size2 and kilo2 and price2 and totalprice2 and isdebt2:
                saveData(2, size2, kilo2, price2, totalprice2, isdebt2)
            if size3 and kilo3 and price3 and totalprice3 and isdebt3:
                saveData(3, size3, kilo3, price3, totalprice3, isdebt3)
            if size4 and kilo4 and price4 and totalprice4 and isdebt4:
                saveData(4, size4, kilo4, price4, totalprice4, isdebt4)
            if size5 and kilo5 and price5 and totalprice5 and isdebt5:
                saveData(5, size5, kilo5, price5, totalprice5, isdebt5)
            return render(request, 'shouhuo.html')
        else:
            return render(request, 'list-shouhuo.html')

class addJinhuoView(View):
    def get(self,request):
        return render(request,'jinhuo.html',{
        })
    def post(self,request):
        purchase_data = request.POST
        if purchase_data['date']:
            purchase_date = purchase_data['date']
        else:
            purchase_date = datetime.now()
        owner = purchase_data['customer']

        size1 = purchase_data['size1']
        number1 = int(purchase_data['number1'])
        kilo1 = int(purchase_data['kilo1'])
        price1 = int(purchase_data['price1'])
        totalprice1 = int(kilo1 * price1)

        size2 = purchase_data['size2']
        number2 = int(purchase_data['number2'])
        kilo2 = int(purchase_data['kilo2'])
        price2 = int(purchase_data['price2'])
        totalprice2 = int(kilo2 * price2)

        size3 = purchase_data['size3']
        number3 = int(purchase_data['number3'])
        kilo3 = int(purchase_data['kilo3'])
        price3 = int(purchase_data['price3'])
        totalprice3 = int(kilo3 * price3)

        size4 = purchase_data['size4']
        number4 = int(purchase_data['number4'])
        kilo4 = int(purchase_data['kilo4'])
        price4 = int(purchase_data['price4'])
        totalprice4 = int(kilo4 * price4)

        size5 = purchase_data['size5']
        number5 = int(purchase_data['number5'])
        kilo5 = int(purchase_data['kilo5'])
        price5 = int(purchase_data['price5'])
        totalprice5 = int(kilo5 * price5)

        total_number = number1 + number2 + number3 + number4 + number5
        total_kilos = kilo1 + kilo2 + kilo3 + kilo4 + kilo5
        total_price = totalprice1 + totalprice2 + totalprice3 + totalprice4 + totalprice5

        def saveData(dataid, size,number,kilo, price, totalprice):
            new_purchase_data = PurchasedataModel()
            new_purchase_data.purchasedata = new_purchase_table
            new_purchase_data.dataid = dataid
            new_purchase_data.size = size
            new_purchase_data.amount = number
            new_purchase_data.kilo = kilo
            new_purchase_data.price = price
            new_purchase_data.totalprice = totalprice
            new_purchase_data.save()

        if owner and total_kilos and total_price:
            new_purchase_table = PurchaseTableModel()
            new_purchase_table.owner = owner
            new_purchase_table.total_amount = total_number
            new_purchase_table.total_kilos = total_kilos
            new_purchase_table.total_price = total_price
            new_purchase_table.add_time = purchase_date
            new_purchase_table.save()
            if size1 and number1 and kilo1 and price1 and totalprice1:
                saveData(1, size1,number1, kilo1, price1, totalprice1)
            if size2 and number2 and kilo2 and price2 and totalprice2:
                saveData(2, size2,number2, kilo2, price2, totalprice2)
            if size3 and number3 and kilo3 and price3 and totalprice3:
                saveData(3, size3,number3, kilo3, price3, totalprice3)
            if size4 and number4 and kilo4 and price4 and totalprice4:
                saveData(4, size4,number4, kilo4, price4, totalprice4)
            if size5 and number5 and kilo5 and price5 and totalprice5:
                saveData(5, size5,number5, kilo5, price5, totalprice5)
            return render(request, 'jinhuo.html')
        else:
            return render(request, 'list-jinhuo.html')

class addHuichuView(View):
    def get(self,request):
        return render(request,'huichu.html',{
        })
    def post(self,request):
        huichu_date = request.POST

        customer1 = huichu_date['customer1']
        money1 = huichu_date['money1']
        if huichu_date['date1']:
            date1 = huichu_date['date1']
        else:
            date1 = datetime.now()

        customer2 = huichu_date['customer2']
        money2 = huichu_date['money2']
        if huichu_date['date2']:
            date2 = huichu_date['date2']
        else:
            date2 = datetime.now()

        customer3 = huichu_date['customer3']
        money3 = huichu_date['money3']
        if huichu_date['date3']:
            date3 = huichu_date['date3']
        else:
            date3 = datetime.now()


        def saveData(customer,money,date):
            new_huichu_data = RemittanceModel()
            new_huichu_data.add_time = date
            new_huichu_data.customer = customer
            new_huichu_data.money = money
            new_huichu_data.save()


        if customer1 and money1 and date1:
            saveData(customer1, money1,date1)
        if customer2 and money2 and date2:
            saveData(customer2, money2,date2)
        if customer3 and money3 and date3:
            saveData(customer3, money3,date3)
        return render(request, 'huichu.html')


class addHuiruView(View):
    def get(self,request):
        return render(request,'huiru.html',{
        })
    def post(self,request):
        huiru_date = request.POST

        customer1 = huiru_date['customer1']
        money1 = huiru_date['money1']
        if huiru_date['date1']:
            date1 = huiru_date['date1']
        else:
            date1 = datetime.now()

        customer2 = huiru_date['customer2']
        money2 = huiru_date['money2']
        if huiru_date['date2']:
            date2 = huiru_date['date2']
        else:
            date2 = datetime.now()

        customer3 = huiru_date['customer3']
        money3 = huiru_date['money3']
        if huiru_date['date3']:
            date3 = huiru_date['date3']
        else:
            date3 = datetime.now()


        def saveData(customer,money,date):
            new_huiru_data = ImportModel()
            new_huiru_data.add_time = date
            new_huiru_data.customer = customer
            new_huiru_data.money = money
            new_huiru_data.save()


        if customer1 and money1 and date1:
            saveData(customer1, money1,date1)
        if customer2 and money2 and date2:
            saveData(customer2, money2,date2)
        if customer3 and money3 and date3:
            saveData(customer3, money3,date3)
        return render(request, 'huiru.html')

class addDangkoukaizhiView(View):
    def get(self,request):
        return render(request,'dangkoukaizhi.html',{
        })
    def post(self,request):
        dangkoukaizhi_date = request.POST

        who1 = dangkoukaizhi_date['who1']
        content1 = dangkoukaizhi_date['content1']
        money1 = dangkoukaizhi_date['money1']
        if dangkoukaizhi_date['date1']:
            date1 = dangkoukaizhi_date['date1']
        else:
            date1 = datetime.now()

        who2 = dangkoukaizhi_date['who2']
        content2 = dangkoukaizhi_date['content2']
        money2 = dangkoukaizhi_date['money2']
        if dangkoukaizhi_date['date2']:
            date2 = dangkoukaizhi_date['date2']
        else:
            date2 = datetime.now()

        who3 = dangkoukaizhi_date['who3']
        content3 = dangkoukaizhi_date['content3']
        money3 = dangkoukaizhi_date['money3']
        if dangkoukaizhi_date['date3']:
            date3 = dangkoukaizhi_date['date3']
        else:
            date3 = datetime.now()

        def saveData(who,money,date,content):
            new_spending_data = SpendingModel()
            new_spending_data.add_time = date
            new_spending_data.who = who
            new_spending_data.content = content
            new_spending_data.money = money
            new_spending_data.save()


        if who1 and money1 and date1 and content1:
            saveData(who1, money1,date1,content1)
        if who2 and money2 and date2 and content2:
            saveData(who2, money2,date2,content2)
        if who3 and money3 and date3 and content3:
            saveData(who3, money3,date3,content3)
        return render(request, 'dangkoukaizhi.html')

class addDebtView(View):
    def get(self,request):
        return render(request,'qiandan.html',{
        })
    def post(self,request):
        dangkoukaizhi_date = request.POST

        customer1 = dangkoukaizhi_date['customer1']
        money1 = dangkoukaizhi_date['money1']
        if dangkoukaizhi_date['date1']:
            date1 = dangkoukaizhi_date['date1']
        else:
            date1 = datetime.now()

        customer2 = dangkoukaizhi_date['customer2']
        money2 = dangkoukaizhi_date['money2']
        if dangkoukaizhi_date['date2']:
            date2 = dangkoukaizhi_date['date2']
        else:
            date2 = datetime.now()

        customer3 = dangkoukaizhi_date['customer3']
        money3 = dangkoukaizhi_date['money3']
        if dangkoukaizhi_date['date3']:
            date3 = dangkoukaizhi_date['date3']
        else:
            date3 = datetime.now()

        def saveData(customer,money,date):
            new_debt_data = DebtModel()
            new_debt_data.add_time = date
            new_debt_data.who = customer
            new_debt_data.money = money
            new_debt_data.save()

        if customer1 and money1 and date1:
            saveData(customer1, money1,date1)
        if customer2 and money2 and date2:
            saveData(customer2, money2,date2)
        if customer3 and money3 and date3 :
            saveData(customer3, money3,date3)
        return render(request, 'qiandan.html')