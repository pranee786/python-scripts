import mysql.connector

def insert(id,name,sal):
    conn = mysql.connector.connect(host='localhost',database='mydb',user='root',password='mastan786')
    if conn.is_connected():
        print('Connected to mysql database')

    # To perform database operations we need cursor
    cursor = conn.cursor()
    try:
        cursor.execute("insert into emp values('%d','%s','%d')"%(id,name,sal))
        conn.commit()
        print('Employee added')
    except Exception as e:
        print(e)
        conn.rollback()

    cursor.close()
    conn.close()

id = int(input('Enter id: '))
name = input('Enter name: ')
sal = int(input('Enter salary: '))
insert(id,name,sal)
