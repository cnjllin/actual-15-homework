#!/usr/bin/env python
#coding:utf-8

import pymysql as mysql

conn = mysql.connect('127.0.0.1','root','root','db',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

def insert(table,field,data):
    sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'ok'}
    else:
        result = {'code':1,'msg':'fail'}
    return result

def list(table,field):
    sql = "select * from %s" % table
    cur.execute(sql)
    res = cur.fetchall()
    for row in res:
        print(row)
    if res:
        user = [{k:row[i] for i,k in enumerate(field)} for row in res]
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'errormsg':'data is null'}
    return result

def getone(table,field,data):
    if data.has_key("username"):
        sql = "select * from %s where username='%s'" % (table,data['username'])
        print sql
    else:
        sql = 'select * from %s where id=%s' % (table,data['id'])
    cur.execute(sql)
    res = cur.fetchone()
    print res
    if res:
        user = {k:res[i] for i,k in enumerate(field)}
        print user
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'errormsg':'data is null'}
    return result

def update(table,field,data):
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = 'update %s set %s where id="%s"' % (table,','.join(conditions),data['id'])
    print(sql)
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'msg':'wrong'}
    return result

def del_user(userid):
        sql = 'delete from user where id=%d' % int(userid)
        cur.execute(sql)
