import mysql.connector

def delete(id):
    conn = mysql.connector.connect(host='localhost',database='mydb',user='root',password='mastan786')
    if conn.is_connected():
        print('Connected to mysql database')

    # To perform database operations we need cursor
    cursor = conn.cursor()
    #str = "delete from emp where id='%d'"
    #args = (id)
    try:
        cursor.execute("delete from emp where id='%d'"%id)
        #cursor.execute(str % args)
        conn.commit()
        print('Employee deleted')
    except:
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

id = int(input('Enter id: '))
delete(id)
