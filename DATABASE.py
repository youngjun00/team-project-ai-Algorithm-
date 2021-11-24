import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS customer (id integer PRIMARY KEY, lapnum text, lapdata text);")

cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('1','DiracDelta(t)')")
cur.execute("INSERT INTO customer(lapnum,lapdata) VALUES('2','Heaviside(t)')")

sql = "select lapdata from customer where lapnum = ?"

cur.execute(sql, ('1'))
rows = cur.fetchall()


for row in rows:
    str = ''.join(row)
    print(str)

conn.close