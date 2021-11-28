import sqlite3 #sqlite 받아오기

conn = sqlite3.connect("test.db") #test.db생성

cur = conn.cursor() #커서생성

cur.execute("CREATE TABLE IF NOT EXISTS customer (id integer PRIMARY KEY, lapnum text, lapdata text);") 
#테이블 생성(primary key 사용 lapnum은 번호, lapdata는 라플라스 변수)
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('1','DiracDelta(t)')")
#lapnum 1 생성, data는 diracdelta(t)생성
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('2','Heaviside(t)')")
#lapnum 2 생성, data는 Heaviside(t)생성
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('3','t*exp(-a*t)')")
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
sql = "select lapdata from customer where lapnum = ?"
cur.execute(sql, ('1'))
rows = cur.fetchall()

#include <math.h>
#include <stdio.h>

from sympy import *
from sympy.plotting.plot import MatplotlibBackend, _matplotlib_list
          
x, y, z, t = symbols('x y z t')
f, g, h = symbols('f, g, h', cls=Function)

init_printing()
# 라플라스 모듈 불러오기 
from sympy.integrals.transforms import laplace_transform
from sympy.integrals.transforms import inverse_laplace_transform

s = symbols('s')
a, w = symbols('a w', constant=True, positive=True)

lapresult = laplace_transform(str, t, s,noconds=True)

lapin = 1
if lapin == 1:
    sql = "select lapdata from customer where lapnum = ?"
    cur.execute(sql, ('1'))
    for row in rows:
        str = ''.join(row)
        print(lapresult)

conn.close