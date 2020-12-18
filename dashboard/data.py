import pandas as pd
import numpy as np
import yfinance as yf
from matplotlib import pyplot as plt
from datetime import timedelta, date
#-----------------------------------------------------------------------------------------------------------------------
End = date.today() + timedelta(2)
End.strftime('%Y-%m-%d')
#-----------------------------------------------------------------------------------------------------------------------
def dataframe_240(ticker):
    data = pd.DataFrame(yf.download(ticker, start='2020-01-01', end=End)['Adj Close'])
    fixed = data.tail(240)
    listed = fixed.values.tolist()
    return listed

PriceList = dataframe_240('SPY')
DaxPriceList = dataframe_240('^GDAXI')
BTCPriceList = dataframe_240('BTCUSD=X')
GOLDPriceList = dataframe_240('GC=F')
OILPriceList = dataframe_240('CL=F')
DXYPriceList = dataframe_240('DX=F')
TLTPriceList = dataframe_240('TLT')
X_ax = [x for x in range(241)]
#-----------------------------------------------------------------------------------------------------------------------

def dataframe_30(ticker):
    data = pd.DataFrame(yf.download(ticker, start='2020-01-01', end=End)['Adj Close'])
    fixed = data.tail(30)
    listed = fixed.values.tolist()
    return listed

PriceList_B = dataframe_30('SPY')
DaxPriceList_B = dataframe_30('^GDAXI')
BTCPriceList_B = dataframe_30('BTCUSD=X')
GOLDPriceList_B = dataframe_30('GC=F')
OILPriceList_B = dataframe_30('CL=F')
DXYPriceList_B = dataframe_30('DX=F')
TLTPriceList_B = dataframe_30('TLT')
X_ax_B = [x for x in range(31)]

#-----------------------------------------------------------------------------------------------------------------------