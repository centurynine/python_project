import pymysql

con = pymysql.connect(host="localhost", database="pythonlab", user="root", password="123456789", charset="utf8")

try :
    cur = con.cursor()

    cur.execute("INSERT INTO customer (first_name,last_name,phone,street,city,province,zipcode) VALUES ('น้ำใส','ใจกล้า','0816857452','12/34 ถ.ประชาอุุทิศ','ห้วยขวาง','กทม.','10310')")
    cur.execute("INSERT INTO customer (first_name,last_name,phone,street,city,province,zipcode) VALUES ('ต้นน้ำ','กล้าหาญ','0829966742','987/542 ซ.สุทธิพร ถ.ประชาสงเคราะห์','ดินแดง','กทม.','10400')")
    cur.execute("INSERT INTO customer (first_name,last_name,phone,street,city,province,zipcode) VALUES ('วันดี','สีสวย','0896652321','2 ถ.พหลโยธิน ต.ประชาธิปัตย์','ธัญบุรี','ปทุมธานี','12130')")
    cur.execute("INSERT INTO customer (first_name,last_name,phone,street,city,province,zipcode) VALUES ('พอใจ','กล้าหาญ','0815252666','20/2 ถ.เทพรัตน แขวงบางนาใต้','บางนา','กทม.','10260')")
    cur.execute("INSERT INTO customer (first_name,last_name,phone,street,city,province,zipcode) VALUES ('วีระ','รักธรรม','0893345687','12 ต.บางพลีใหญ่','บางพลี','สมุทรปราการ','10540')")

    con.commit() #ยืนยันการเปลี่ยนแปลงข้อมูล
    print("เพิ่มข้อมูลลงในตารางข้อมูลเรียบร้อยแล้ว")

    cur.close()  # สั่งปิดเคอร์เซอร์
except :
    con.rollback() # ยกเลิกการทำคำสั่ง sql และดึงข้อมูลเดิมกลับมา
    print("ไม่สามารถเพิ่มข้อมูลลงในตารางข้อมูลได้")
finally :
    con.close() # สั่งปิดการเชื่อมต่อกับฐานข้อมูล