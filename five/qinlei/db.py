# coding:utf-8
from apps import app
import pymysql as mysql

host = app.config.get('SQL_HOST')
user = app.config.get('SQL_USER')
passwd = app.config.get('SQL_PASSWD')
db = app.config.get('SQL_DB')

conn = mysql.connect(user=user, passwd=passwd, host=host, db=db, charset='utf8')
conn.autocommit(True) #开启提交事务
cur = conn.cursor()

def query(tname, args,id=None):
    users = []
    if not id:
        sql = "select %s from %s" %(','.join(args),tname)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            user = {}
            for i,k in enumerate(args):
                user[k] = row[i]
            users.append(user)
        return users
    else:
        sql = "select %s from %s where id = '%s'" %(','.join(args),tname,id)
        cur.execute(sql)
        result = cur.fetchone()
        user = {}
        for k,v in enumerate(args):
            user[v] = result[k]
        users.append(user)
        return users

def adduser(tname, args):
    sql = "insert into %s set %s" %(tname,','.join(args))
    cur.execute(sql)

def delete(tname, id):
    sql = "delete from %s where id='%s'" % (tname, id)
    cur.execute(sql)

def update(tname,args,id):

    sql = "update %s set %s where id='%s'"%(tname,','.join(args),id)
    
    cur.execute(sql)
