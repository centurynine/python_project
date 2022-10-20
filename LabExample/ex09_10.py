# Sql เพ่ิมข้อมูล 1 รายการ ก่อนที่จะทดลองลบ
# "INSERT INTO customer (first_name,last_name,phone,street,city,province,zipcode) VALUES ('เอก','วิศวกรรม','0893345687','39 ม.1','ธัญบุรี','ปทุมธานี','12110')"

import pymysql

con = pymysql.connect(host="localhost", database="testmariab", user="root", password="1234", charset="utf8")

try :
    cur = con.cursor()
    cur.execute("DELETE FROM customer WHERE cust_id = 6")

    con.commit()
    print("ลบข้อมูลลูกค้าสำเร็จแล้ว")

    cur.close()
except :
    con.rollback()
    print("ไม่สามารถลบข้อมูลในตารางข้อมูลได้")
finally :
    con.close()