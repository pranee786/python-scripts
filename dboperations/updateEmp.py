import mysql.connector

def update(id,sal):
    conn = mysql.connector.connect(host='localhost',database='mydb',user='root',password='mastan786')
    if conn.is_connected():
        print('Connected to mysql database')

    # To perform database operations we need cursor
    cursor = conn.cursor()
    try:
        cursor.execute("update emp set sal='%d' where id='%d'"%(sal,id))
        conn.commit()
        print('Employee updated')
    except Exception as e:
        print(e)
        conn.rollback()

    cursor.close()
    conn.close()

id = int(input('Enter id: '))
sal = int(input('Enter salary: '))
update(id,sal)
