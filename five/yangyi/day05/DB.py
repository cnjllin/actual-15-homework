# Author: tailorYang

import mysql.connector as mysql

#连接数据库
def connect():
    conn = mysql.connect(
        user='root',
        password='yangyi',
        database='reboot15',
        charset = 'utf8'
    )
    cursor = conn.cursor()
    return conn,cursor

def execute(sql,action):
    conn , cursor = connect()
    cursor.execute(sql)
    if action.lower() =='select':
        result = cursor.fetchall()
    else:
        result = str(cursor.rowcount)
        conn.commit()
    cursor.close()
    conn.close()
    return result




