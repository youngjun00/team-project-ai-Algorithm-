from tkinter import *
from sympy import *
from sympy.plotting.plot import MatplotlibBackend, _matplotlib_list
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

x, y, z, t = symbols('x y z t')
f, g, h = symbols('f, g, h', cls=Function)

init_printing()

from sympy.integrals.transforms import laplace_transform

s = symbols('s')
a, w = symbols('a w', constant=True, positive=True)

lapin=0
root = Tk()
root.title("라플라스 변환 계산기")
sql = "select lapdata from customer where lapnum = ?"

root.geometry("600x600")
def btn1():
    lapin=1
    print(lapin)
    
def btn2():
    lapin=2
    print(lapin)
    
def btn3():
    lapin=3
    print(lapin)
    
def btn4():
    lapin=4
    print(lapin)
    
def btn5():
    lapin=5
    print(lapin)
    
def btn6():
    lapin=6
    print(lapin)
    
def btn7():
    lapin=7
    print(lapin)
    
def btn8():
    lapin=8
    print(lapin)
    
def btn9():
    lapin=9
    print(lapin)
    
def btn10():
    lapin=10
    print(lapin)
    
def btn11():
    if lapin == 1:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('1'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True)
    elif lapin == 2:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('2'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True)
    elif lapin == 3:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('3'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True)
    elif lapin == 4:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('4'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True) 
    elif lapin == 5:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('5'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True)  
    elif lapin == 6:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('6'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True)
    elif lapin == 7:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('7'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True)  
    elif lapin == 8:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('8'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True)
    elif lapin == 9:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('9'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True) 
    elif lapin == 10:
        sql = "select lapdata from customer where lapnum = ?"
        cur.execute(sql, ('10'))
        rows = cur.fetchall()
        for row in rows:
            str1 = ''.join(row)
            lapresult = laplace_transform(str1, t, s,noconds=True)
    labelresulte.config(text = lapresult)
    print(lapresult)
    
b1 = Button(root,width=6, height=3, text='1/s',command=btn1)
b1.grid(row=0,column=0)
b2 = Button(root,width=6, height=3, text='1/s',command=btn2)
b2.grid(row=0,column=1)
b3 = Button(root,width=6, height=3, text='1/s',command=btn3)
b3.grid(row=0,column=2)
b4 = Button(root,width=6, height=3, text='1/s',command=btn4)
b4.grid(row=1,column=0)
b5 = Button(root,width=6, height=3, text='1/s',command=btn5)
b5.grid(row=1,column=1)
b6 = Button(root,width=6, height=3, text='1/s',command=btn6)
b6.grid(row=1,column=2)
b7 = Button(root,width=6, height=3, text='1/s',command=btn7)
b7.grid(row=2,column=0)
b8 = Button(root,width=6, height=3, text='1/s',command=btn8)
b8.grid(row=2,column=1)
b9 = Button(root,width=6, height=3, text='1/s',command=btn9)
b9.grid(row=2,column=2)
b10 = Button(root,width=6, height=3, text='1/s',command=btn10)
b10.grid(row=3,column=0)
b11 = Button(root,width=6, height=3, text='변환',command=btn11)
b11.grid(row=3,column=1)

labelresulte = Label(root, text = "답")
labelresulte.grid(row=3,column=2)

root.mainloop
conn.close