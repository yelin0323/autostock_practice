from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI','2000-01-04') #다우존스 지수
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')   #코스피 지수

#비교를 위해서 지수화 해준다.
d = (dow.Close / dow.Close.loc['2000-01-04']) * 100 #지수화
k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100 #지수화

import matplotlib.pyplot as plt
plt.figure(figsize=(9,5))
plt.plot(d.index, d, 'r--', label = 'Dow Jones Industrial Average')
plt.plot(k.index, k, 'b', label = 'KOSPI')
plt.grid(True)
plt.legend(loc='best')
plt.show()
