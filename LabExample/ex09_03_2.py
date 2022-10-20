import pymysql

con = pymysql.connect(host="127.0.0.1", database="world", user="root", password="1234", charset="utf8")
pop_value = 200_000_000    # ใน python สามารถกำหนดค่า โดใช้ underscore เพื่อให้คนอ่าน่าได้ง่าย

try:
    cur = con.cursor()
    cur.execute('SELECT * FROM world.country WHERE population > '+ str(pop_value) + ' LIMIT 10;')
    data = cur.fetchall()
    
    for i in data:
        print(i[1], i[4])
 
except:
    print("มี Error")

finally:
    con.close() 