import pandas as pd
import yfinance as yf
from datetime import timedelta, date

End = date.today() + timedelta(2)
End.strftime('%Y-%m-%d')

def pct_increase(TICKER):
    DF = pd.DataFrame(yf.download(TICKER, start='2020-01-01', end=End)['Adj Close'])
    Fixed = DF.tail(240)
    Start = Fixed.iloc[0]
    Final = Fixed.iloc[-1]
    Sum = ((Final/Start)*100)-100
    return Sum

SP = 'SPY'
DA = '^GDAXI'
BT = 'BTCUSD=X'
GD = 'GC=F'
OI = 'CL=F'
DY = 'DX=F'
TL = 'TLT'

def callit(TICKER):
    Call = pct_increase(TICKER).round(2)[0]
    return Call

SPY = callit(SP)
DAX = callit(DA)
BTC = callit(BT)
GLD = callit(GD)
OIL = callit(OI)
DXY = callit(DY)
TLT = callit(TL)

def pct_increaseB(TICKER):
    DF = pd.DataFrame(yf.download(TICKER, start='2020-01-01', end=End)['Adj Close'])
    Fixed = DF.tail(30)
    Start = Fixed.iloc[0]
    Final = Fixed.iloc[-1]
    Sum = ((Final/Start)*100)-100
    return Sum

SP_B = 'SPY'
DA_B = '^GDAXI'
BT_B = 'BTCUSD=X'
GD_B = 'GC=F'
OI_B = 'CL=F'
DY_B = 'DX=F'
TL_B = 'TLT'

def callitB(TICKER):
    Call = pct_increaseB(TICKER).round(2)[0]
    return Call

SPY_B = callitB(SP_B)
DAX_B = callitB(DA_B)
BTC_B = callitB(BT_B)
GLD_B = callitB(GD_B)
OIL_B = callitB(OI_B)
DXY_B = callitB(DY_B)
TLT_B = callitB(TL_B)