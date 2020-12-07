from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt 

yf.pdr_override()

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')   #코스피 지수 데이터를 받아온다

window = 252 #window는 1년동안의 대략적인 개장일
peak = kospi['Adj Close'].rolling(window, min_periods=1).max() #종가 컬럼에서 1년 기간 단위로 최고치(peak)를 구한다
drawdown = kospi['Adj Close']/peak-1.0 #최고치(peak) 대비 현재 KOSPI 종가가 얼마나 하락했는지 구한다
max_dd = drawdown.rolling(window, min_periods=1).min() #drawdown에서 1년 기간단위로 최저치(최대 손실 낙폭)를 구한다

plt.figure(figsize=(9,7))
plt.subplot(211) #2행 1열 중 1행에 그린다
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212)
drawdown.plot(c='blue', label='KOSPI DD', grid = True, legend= True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()