#!/usr/bin/python
# --*-- coding:UTF-8 --*--
def db_cursor():
    import MySQLdb as mysql
    db=mysql.connect(host='localhost',user='root',passwd='',port=3306,db='51reboot',charset='utf8')
    return db.cursor()

if __name__ == '__main__':
    cur=db_cursor()
    sql='select * from user'
    cur.execute(sql)
    print cur.fetchall()
