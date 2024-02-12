import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES(1,'FAITH KARIMI',34,340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(2,'ZEEOX CREAMY',12,340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(3,'ALEX ORLAND',27,850000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(4,'PETER TOSH',41,560000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(5,'VENUS JUPITER',23,345000.00)")

conn.commit()
print("Employee inserted successfully")
conn.close()