import pymysql

dbhost = 'localhost'
dbname = 'world'
dbuser = 'root'
dbpasswd = '1234'
charset = 'utf8'

con = pymysql.connect(
    host=dbhost, 
    database=dbname, 
    user=dbuser, 
    password=dbpasswd, 
    charset=charset
)

try:
    cur = con.cursor()
    cur.execute('SHOW DATABASES;')

    data = cur.fetchall()
    for i in data:
        print(f'{i[0]}')

except:
    print("มี Error")

finally:
    con.close() 


