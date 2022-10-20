import pymysql

con = pymysql.connect(host="127.0.0.1", database="pythonlab", user="root", password="123456789", charset="utf8")

try:
    cur = con.cursor()
    cur.execute('SELECT VERSION();')
    data = cur.fetchall()
    
    for i in data:
        print(f'MySQL Version : {i[0]}')
 
except:
    print("มี Error")

finally:
    con.close() # สั่งปิดการเชื่อมต่อกับฐานข้อมูล


