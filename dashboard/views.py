from django.shortcuts import render
from .models import *
from .data import *
from .performance import SPY, DAX, BTC, GLD, OIL, DXY, TLT, SPY_B, DAX_B, BTC_B, GLD_B, OIL_B, DXY_B, TLT_B
#-----------------------------------------------------------------------------------------------------------------------
def spy(request):
    SPYprice = PriceList
    x = X_ax
    performance = SPY
    context = {'price': SPYprice, 'x': x, 'performance': performance}
    return render(request, 'spy.html', context)

def dax(request):
    DAXprice = DaxPriceList
    x = X_ax
    performance = DAX
    context = {'price': DAXprice, 'x': x, 'performance': performance}
    return render(request, 'dax.html', context)

def btc(request):
    BTCprice = BTCPriceList
    x = X_ax
    performance = BTC
    context = {'price': BTCprice, 'x': x, 'performance': performance}
    return render(request, 'btc.html', context)

def gold(request):
    GOLDprice = GOLDPriceList
    x = X_ax
    performance = GLD
    context = {'price': GOLDprice, 'x': x, 'performance': performance}
    return render(request, 'gold.html', context)

def oil(request):
    OILprice = OILPriceList
    x = X_ax
    performance = OIL
    context = {'price': OILprice, 'x': x, 'performance': performance}
    return render(request, 'oil.html', context)

def dxy(request):
    DXYprice = DXYPriceList
    x = X_ax
    performance = DXY
    context = {'price': DXYprice, 'x': x, 'performance': performance}
    return render(request, 'dxy.html', context)

def tlt(request):
    TLTprice = TLTPriceList
    x = X_ax
    performance = TLT
    context = {'price': TLTprice, 'x': x, 'performance': performance}
    return render(request, 'tlt.html', context)

#-----------------------------------------------------------------------------------------------------------------------

def spy30(request):
    SPYPrice = PriceList_B
    x = X_ax_B
    performance = SPY_B
    context = {'price': SPYPrice, 'x': x, 'performance': performance}
    return render(request, 'spy30.html', context)

def dax30(request):
    DAXPrice = DaxPriceList_B
    x = X_ax_B
    performance = DAX_B
    context = {'price': DAXPrice, 'x': x, 'performance': performance}
    return render(request, 'dax30.html', context)

def btc30(request):
    BTCPrice = BTCPriceList_B
    x = X_ax_B
    performance = BTC_B
    context = {'price': BTCPrice, 'x': x, 'performance': performance}
    return render(request, 'btc30.html', context)

def gold30(request):
    GOLDPrice = GOLDPriceList_B
    x = X_ax_B
    performance = GLD_B
    context = {'price': GOLDPrice, 'x': x, 'performance': performance}
    return render(request, 'gold30.html', context)

def dxy30(request):
    DXYPrice = DXYPriceList_B
    x = X_ax_B
    performance = DXY_B
    context = {'price': DXYPrice, 'x': x, 'performance': performance}
    return render(request, 'dxy30.html', context)

def oil30(request):
    OILPrice = OILPriceList_B
    x = X_ax_B
    performance = OIL_B
    context = {'price': OILPrice, 'x': x, 'performance': performance}
    return render(request, 'oil30.html', context)

def tlt30(request):
    TLTPrice = TLTPriceList_B
    x = X_ax_B
    performance = TLT_B
    context = {'price': TLTPrice, 'x': x, 'performance': performance}
    return render(request, 'tlt30.html', context)