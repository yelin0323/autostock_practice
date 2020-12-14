import pymysql

connection = pymysql.connect(host='localhost', port=3306, db='INVESTAR', 
    user='root', passwd='dpfls7708', autocommit=True)  

cursor = connection.cursor()    #cursor 객체를 생성
cursor.execute("SELECT VERSION();")     # cursor 객체의 execute()함수를 사용해 select문을 실행
result = cursor.fetchone()  #fetchone 함수를 사용해 실행 결과를 튜플로 받는다.

print ("MariaDB version : {}".format(result))

connection.close()