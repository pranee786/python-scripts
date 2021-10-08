import mysql.connector

conn = mysql.connector.connect(host='localhost',database='mydb',user='root',password='mastan786')
if conn.is_connected():
    print('Connected to mysql database')

# To perform database operations we need cursor
cursor = conn.cursor()
cursor.execute('select * from emp')
# To fetch one record at a time
    #row = cursor.fetchone()
    #while row is not None:
        #print(row)
        #row = cursor.fetchone()

# To fetch all records all a time
row = cursor.fetchall()
print('Total number of records',cursor.rowcount)
for r in row:
    print(row)

cursor.close()
conn.close()
