import pymysql

con = pymysql.connect(host="127.0.0.1", database="world", user="root", password="1234", charset="utf8")
try:
    cur = con.cursor()
    cur.execute('SELECT * FROM world.country WHERE population > 200000000 LIMIT 10;')
    data = cur.fetchall()
    
    for i in data:
        print(i[1], i[4])
 
except:
    print("มี Error")

finally:
    con.close() 