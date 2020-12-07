from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
yf.pdr_override()

dow = pdr.get_data_yahoo('^DJI','2000-01-04') #다우존스 지수
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')   #코스피 지수


df = pd.DataFrame({'DOW': dow['Close'], 'KOSPI': kospi['Close']}) #다우존스 지수의 종가 칼럼과 코스피 지수의 종가 칼럼으로 데이터 프레임 생성
df = df.fillna(method='bfill') #데이터 프레임 생성 시 생긴 NaN을 제거
df = df.fillna(method='ffill')


plt.figure(figsize=(7,7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.xlabel('Dow Jones Industrial Average')
plt.ylabel('KOSPI')
plt.show()
