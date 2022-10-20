import pymysql

id = input("กรุณากรอกรหัสลูกค้า : ")
sql = "SELECT * FROM customer WHERE cust_id = "+id
con = pymysql.connect(host="localhost", database="testmariab", user="root", password="1234", charset="utf8")

try :
    cur = con.cursor()
    cur.execute(sql)

    cust_data = cur.fetchone()
    if(str(cust_data) in "None") :
        print("ไม่พบข้อมูลลูกค้าตามรหัสลูกค้าที่ระบุ")
    else :
        print("รหัสลูกค้า : ",cust_data[0])
        print("ชื่อ-นามสกุล :  ",cust_data[1],cust_data[2])
        print("เขตที่อยู่ : ",cust_data[5])
    cur.close()

except :
    print("ไม่สามารถเรียกดึงข้อมูลจากฐานข้อมูลได้")
finally :
    con.close()