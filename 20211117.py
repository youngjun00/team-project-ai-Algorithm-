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
lap1 =1 
if lap1 == 2:
   laplace_transform(Heaviside(t), t, s, noconds=True)##Heaviside(t)=u(t)  2번
elif lap1 == 3:
   laplace_transform( t*exp(-a*t), t, s, noconds=True)## 7번 
elif lap1 == 4:
   laplace_transform(sin(w*t), t, s, noconds=True )## 8번
elif lap1 == 5:
   laplace_transform(cos(w*t), t, s, noconds=True )## 9번
elif lap1 == 6:
   laplace_transform( sinh(w*t), t, s, noconds=True)## 10번
#elif lap1 == 7:
#laplace_transform( cosh(w*t), t, s, noconds=True)## 11번 해결안됨.
elif lap1 == 8:
   laplace_transform(t * sin(w*t), t, s, noconds=True )## 12번
elif lap1 == 9:
   laplace_transform(t * cos(w*t), t, s, noconds=True )## 13번
elif lap1 == 10:
   laplace_transform(exp(-a*t) * sin(w*t), t, s, noconds=True) ## 14번
elif lap1 == 11:
   laplace_transform(exp(-a*t) * cos(w*t), t, s, noconds=True )## 15번



import sqlite3
 
# DB 생성 (오토 커밋)
conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXITS customer (idinteger PRIMARY KEY , lapnum text, lapdata text);")

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('1','Heaviside(t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('2','t*exp(-a*t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('3','sin(w*t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('4','cos(w*t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('5','sinh(w*t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('6','t * sin(w*t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('7','t * cos(w*t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('8','exp(-a*t) * sin(w*t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('9','(exp(-a*t) * cos(w*t)')")

sp1 = "select lapdata from customer where lapnum = ?"

if num = 1:
   cur.execute(sp1,('1'))
   rows = cur.fetchall()

for row in rows:
   print(row)

conn.close

laplace_transform( DiracDelta(t), t, s,noconds=True)

import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customer (id integer PRIMARY KEY, lapnum text, lapdata text);")

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('1','DiracDelta(t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('2','Heaviside(t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('1','DiracDelta(t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('2','Heaviside(t)')")

sql = "select lapdata from customer where lapnum = ?"

cur.execute(sql, ('1'))
rows = cur.fetchall()


for row in rows:
    str = ''.join(row)
    print(str)

laplace_transform(str, t, s,noconds=True)
conn.close