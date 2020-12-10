from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from matplotlib import pyplot as plt
import mplfinance as mpf 

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_ = 'pgRR')
    s = str(pgrr.a['href']).split('=') #s는 =을 기준으로 3개로 나누어진다.
    last_page = s[-1]


    df = pd.DataFrame()
    sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

    for page in range(1, int(last_page)+1):
        page_url = '{}&page={}'.format(sise_url, page)
        df = df.append(pd.read_html(page_url, header = 0)[0])

    df = df.dropna()
    df = df.iloc[0:30]
    df = df.rename(columns={'날짜' : 'Date', '시가' : 'Open', '고가' : 'High', '저가' : 'Low', '종가' : 'Close', '거래량' : 'Volume'})
    df = df.sort_values(by = 'Date')
    df.index = pd.to_datetime(df.Date)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

    kwargs = dict(title = 'Celltrion candle chart', type = 'candle', mav=(2,4,6), volume=True, ylabel='ohlc candles')
    mc = mpf.make_marketcolors(up = 'r', down = 'b', inherit=True) #마켓 색상을 상승은 빨간색, 하락은 파란색으로 지정하고 관련 색상은 이를 따른다.
    s = mpf.make_mpf_style(marketcolors=mc) #스타일 객체를 생성
    mpf.plot(df, **kwargs, style=s)




