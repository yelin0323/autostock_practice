import pandas as pd

#krx_list = pd.read_html('C:/python32/stockauto/상장법인목록.xls')
#krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format) #종목코드를 6자리로 (앞에 빈자리는 0으로 채우기)
#print (krx_list[0])

krx_list = pd.read_html('C:/python32/stockauto/상장법인목록.xls')[0] #함수 뒤에 [0]을 붙여서 결과값을 데이터프레임으로 받는다
krx_list['종목코드'] = krx_list['종목코드'].map('{:06d}'.format) #종목코드를 6자리로 (앞에 빈자리는 0으로 채우기)
krx_list = krx_list.sort_values(by = '종목코드')
print (krx_list)
