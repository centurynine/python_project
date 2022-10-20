import pymysql

con = pymysql.connect(host="localhost", database="testmariab", user="root", password="1234", charset="utf8")

try :
    cur = con.cursor()
    cur.execute("SELECT * FROM customer")

    # นำผลลัพธ์ 1 รายการที่ sql statement เรียกดึงข้อมูลได้ มาเก็บลงตัวแปร cust_data
    cust_data = cur.fetchone()
    print(cust_data)

    cur.close()
except :
    print("ไม่สามารถเรียกดึงข้อมูลจากฐานข้อมูลได้")
finally :
    con.close()
    