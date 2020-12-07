from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt 

yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
sec_dpc = (sec['Close']/sec['Close'].shift(1)-1) * 100  #일간 변동률 구하기
sec_dpc.iloc[0] = 0
sec_dpc_cs = sec_dpc.cumsum()   #일간 변동률 누적합 구하기

msft = pdr.get_data_yahoo('MSFT', start = '2018-05-04')
msft_dpc = (msft['Close']/msft['Close'].shift(1)-1) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cs = msft_dpc.cumsum()
tmp_msft = msft.drop(columns='Volume')

plt.plot(sec.index, sec_dpc_cs, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc_cs, 'r--', label="Microsoft")
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()
