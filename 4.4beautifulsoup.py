from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_ = 'pgRR')
    s = str(pgrr.a['href']).split('=') #s는 =을 기준으로 3개로 나누어진다.
    last_page = s[-1]

    print(pgrr.prettify())  #pgrr의 getText 속성값을 계층적으로 출력
    print(last_page)

    df = pd.DataFrame()
    sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

    for page in range(1, int(last_page)+1):
        page_url = '{}&page={}'.format(sise_url, page)
        df = df.append(pd.read_html(page_url, header = 0)[0])

    df = df.dropna()

    print(df)