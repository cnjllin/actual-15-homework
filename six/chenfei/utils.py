#!/usr/bin/python
# __*__ conding: UTF-8 __*__


import MySQLdb as mysql

conn = mysql.connect('127.0.0.1','root','123456','cf123',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

def insert(table,field,data):
    sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'insert ok'}
    else:
        result = {'code':1,'msg':'insert fail'}
    return result

def list(table,field):
    sql = "select * from %s" % table
    cur.execute(sql)
    res = cur.fetchall()
    if res:
       user = [{k:row[i] for i,k in enumerate(field)} for row in res]
       result = {'code':0,'msg':user}
    else:
       result = {'code':1,'errmsg':'data is null'}
    return result

def getone(table,field,data):
    if data.has_key("username"):
         sql = 'select * from %s where username="%s"' % (table,data['username'])
    else:
         sql = 'select * from %s where id="%s"' % (table,data['id'])
    cur.execute(sql)
    res = cur.fetchone()
    if res:
       user = {k:res[i] for i,k in enumerate(field)}
       result = {'code':0,'msg':user}
    else:
       result = {'code':1,'msg':"data is null"}
    return result

def update(table,field,data):
    condition = ["%s='%s'"%(k,data[k]) for k in data]
    sql = "update %s set %s where id='%s';"%(table,','.join(condition),data['id'])
    cur.execute(sql)
    res = cur.fetchone()
    if not res:
        result = {'code':0,'msg':'update ok'}
    else:
       result = {'code':1,'msg':'update fail'}
    return result 


def delete(data):
    sql = "delete from  user  where id='%s';"%(data['id'])
    cur.execute(sql)
