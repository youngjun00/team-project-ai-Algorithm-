from tkinter import * #tkinter 모듈 
from sympy import * # sympy 모듈 불러오기
import sqlite3 #sqlite 받아오기

conn = sqlite3.connect("test.db") #test.db생성
cur = conn.cursor() #커서생성

cur.execute("CREATE TABLE IF NOT EXISTS customer (id integer PRIMARY KEY, lapnum text, lapdata text);") 
#테이블 생성(primary key 사용 lapnum은 번호, lapdata는 라플라스 변수)

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('1','DiracDelta(t)')")
#lapnum 1 생성, data는 diracdelta(t)생성

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('2','Heaviside(t)')")
#lapnum 2 생성, data는 Heaviside(t)생성

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('3','exp(-a*t)')")
#lapnum 3 생성, data는 t*exp(-a*t)생성

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('4','sin(w*t)')")
#lapnum 4 생성, data는 sin(w*t)생성

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('5','sinh(w*t)')")
#lapnum 5 생성, data는 sinh(w*t)생성

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('6','cosh(w*t)')")
#lapnum 6 생성, data는 cosh(w*t)생성

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('7','t * sin(w*t)')")
#lapnum 7 생성, data는 t * sin(w*t)생성

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('8','t * cos(w*t)')")
#lapnum 8 생성, data는 t * cos(w*t)생성

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('9','exp(-a*t) * sin(w*t)')")
#lapnum 9 생성, data는 exp(-a*t) * sin(w*t)생성

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('10','exp(-a*t) * cos(w*t)')")
#lapnum 10 생성, data는 exp(-a*t) * cos(w*t)생성

x, y, z, t = symbols('x y z t') # 기호변수 생성(x,y,z,t)
f, g, h = symbols('f, g, h', cls=Function) # 기호변수 생성(f,g,h)

init_printing() # 수식출력을 LaTex수식으로 출력한다

from sympy.integrals.transforms import laplace_transform # 라플라스 변환 모듈 불러오기

s = symbols('s') # 변수 생성
a, w = symbols('a w', constant=True, positive=True) # 변수생성 (a,w)

lapin=0 # 라플라스 계산기 변수 생성
root = Tk() #gui 생성
root.title("라플라스 변환 계산기") #gui 타이틀 생성
sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐

root.geometry("600x600") #gui 계산기 크기 600*600 생성
def btn1(): #버튼1번이 눌렸을때
    lapin=1 #계산기 입력 변수를 1로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
    
def btn2(): #버튼2번이 눌렸을때
    lapin=2 #계산기 입력 변수를 2로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
    
def btn3(): #버튼3번이 눌렸을때
    lapin=3 #계산기 입력 변수를 3로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
    
def btn4(): #버튼4번이 눌렸을때
    lapin=4 #계산기 입력 변수를 4로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
    
def btn5(): #버튼5번이 눌렸을때
    lapin=5 #계산기 입력 변수를 5로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
    
def btn6(): #버튼6번이 눌렸을때
    lapin=6 #계산기 입력 변수를 6로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
    
def btn7(): #버튼7번이 눌렸을때
    lapin=7 #계산기 입력 변수를 7로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
    
def btn8(): #버튼8번이 눌렸을때
    lapin=8 #계산기 입력 변수를 8로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
     
def btn9(): #버튼9번이 눌렸을때
    lapin=9 #계산기 입력 변수를 9로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
    
def btn10(): #버튼10번이 눌렸을때
    lapin=10 #계산기 입력 변수를 10으로하여 if문 사용
    print(lapin) #계산기 입력값 확인용 프린트
    
def btn11(): #버튼11번이 눌렸을때
    if lapin == 1: #입력변수가 1일때
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('1')) #데이터베이스 1번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True)
    
    elif lapin == 2:
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('2')) #데이터베이스 2번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True)
    
    elif lapin == 3:
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('3')) #데이터베이스 3번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True) #lapresult에 라플라스 변환 값을 입력
    
    elif lapin == 4:
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('4')) #데이터베이스 4번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True) #lapresult에 라플라스 변환 값을 입력
    
    elif lapin == 5:
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('5')) #데이터베이스 5번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True)  #lapresult에 라플라스 변환 값을 입력
    
    elif lapin == 6:
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('6')) #데이터베이스 6번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True)  #lapresult에 라플라스 변환 값을 입력
    
    elif lapin == 7:
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('7')) #데이터베이스 7번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True)  #lapresult에 라플라스 변환 값을 입력
    
    elif lapin == 8:
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('8')) #데이터베이스 8번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True) #lapresult에 라플라스 변환 값을 입력
    
    elif lapin == 9:
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('9')) #데이터베이스 9번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True)  #lapresult에 라플라스 변환 값을 입력
    
    elif lapin == 10:
        sql = "select lapdata from customer where lapnum = ?" #sql변수를 이용해 데이터 베이스에서 찾을 값을 선정 lapnum에 따라 값이 달라짐
        cur.execute(sql, ('10')) #데이터베이스 10번항목의 값을 값으로 지정
        rows = cur.fetchall() #rows변수생성
        for row in rows: #rows변수를 row에 전송
            str1 = ''.join(row) #row값을str1에 데이터형식을 변경하여 입력
            lapresult = laplace_transform(str1, t, s,noconds=True) #lapresult에 라플라스 변환 값을 입력
    labelresulte.config(text = lapresult) #결과출력창에 lapresult 데이터를 전송
    ## 현재 이부분에서 라플라스변수는 text 형식이아닌 sympy 내부의 변수입니다. 그런데 이 변수를 출력할 방법을 찾지못했습니다.
    print(lapresult) #입력값 터미널로 확인
    
b1 = Button(root,width=6, height=3, text='1/s',command=btn1) #버튼 1번생성 command는 눌려졌을때 변수를 확인하는데 사용
b1.grid(row=0,column=0) #버튼 위치 배치(row,column)

b2 = Button(root,width=6, height=3, text='1/s',command=btn2) #버튼 2번생성 command는 눌려졌을때 변수를 확인하는데 사용
b2.grid(row=0,column=1) #버튼 위치 배치(row,column)

b3 = Button(root,width=6, height=3, text='1/s',command=btn3) #버튼 3번생성 command는 눌려졌을때 변수를 확인하는데 사용
b3.grid(row=0,column=2) #버튼 위치 배치(row,column)

b4 = Button(root,width=6, height=3, text='1/s',command=btn4) #버튼 4번생성 command는 눌려졌을때 변수를 확인하는데 사용
b4.grid(row=1,column=0) #버튼 위치 배치(row,column)
 
b5 = Button(root,width=6, height=3, text='1/s',command=btn5) #버튼 5번생성 command는 눌려졌을때 변수를 확인하는데 사용
b5.grid(row=1,column=1) #버튼 위치 배치(row,column)

b6 = Button(root,width=6, height=3, text='1/s',command=btn6) #버튼 6번생성 command는 눌려졌을때 변수를 확인하는데 사용
b6.grid(row=1,column=2) #버튼 위치 배치(row,column)

b7 = Button(root,width=6, height=3, text='1/s',command=btn7) #버튼 7번생성 command는 눌려졌을때 변수를 확인하는데 사용
b7.grid(row=2,column=0) #버튼 위치 배치(row,column)

b8 = Button(root,width=6, height=3, text='1/s',command=btn8) #버튼 8번생성 command는 눌려졌을때 변수를 확인하는데 사용
b8.grid(row=2,column=1) #버튼 위치 배치(row,column)

b9 = Button(root,width=6, height=3, text='1/s',command=btn9) #버튼 9번생성 command는 눌려졌을때 변수를 확인하는데 사용
b9.grid(row=2,column=2) #버튼 위치 배치(row,column)

b10 = Button(root,width=6, height=3, text='1/s',command=btn10) #버튼 10번생성 command는 눌려졌을때 변수를 확인하는데 사용
b10.grid(row=3,column=0) #버튼 위치 배치(row,column)

b11 = Button(root,width=6, height=3, text='변환',command=btn11) #버튼 11번생성 command는 눌려졌을때 변수를 확인하는데 사용 
b11.grid(row=3,column=1) #버튼 위치 배치(row,column)

labelresulte = Label(root, text = "답") #출력창 생성
labelresulte.grid(row=3,column=2) #버튼 위치 배치(row,column)

root.mainloop #계속 
conn.close #conn을 마무리(저장)
