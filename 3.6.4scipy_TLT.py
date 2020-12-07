from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
yf.pdr_override()
from scipy import stats

tlt = pdr.get_data_yahoo('TLT','2000-01-04') #다우존스 지수
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')   #코스피 지수

df = pd.DataFrame({'X': tlt['Close'], 'Y': kospi['Close']}) #다우존스 지수의 종가 칼럼과 코스피 지수의 종가 칼럼으로 데이터 프레임 생성
df = df.fillna(method='bfill') #데이터 프레임 생성 시 생긴 NaN을 제거
df = df.fillna(method='ffill')

regr = stats.linregress(df.X, df.Y)
regr_line = f'Y={regr.slope:.2f} * X + {regr.intercept:.2f}'


plt.figure(figsize=(7,7))
plt.plot(df.X, df.Y, 'g.')
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
plt.legend(['TLT x KOSPI', regr_line])
plt.title(f'TLT x KOSPI (R={regr.rvalue:.2f})')
plt.xlabel('iShares Barclays 20 + Yr Treas.Bond (TLT)')
plt.ylabel('KOSPI')
plt.show()
