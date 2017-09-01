
#! /bin/env python
#coding:utf-8
from flask import Flask,render_template,request
import MySQLdb as mysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')

conn= mysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='reboot15',charset='utf8')
conn.autocommit(True)
cur=conn.cursor()


def insert (table,field,data):
    sql="insert into %s (%s) value (%s)" % (table,','.join(field),data['user_name'])
    cur.execute(sql)
    result={'code':0,'errmsg':'ok'}
    return result


def list(table,field):
    sql="select * from %s " % table
    cur.execute(sql)
    res=cur.fetchall()
    if not res:
        result={'code':1,'errmsg':'data is null'}
        return result
    else:
        user={k:row[i] for i,k in enumerate(field) for row in user}
        return user


def getone(table,field):
    sql="select * from %s wher id=%s " % (table,uid)
    cur.execute(sql)
    res=cur.fetchall()
    if not res:
        result={'code':1,'errmsg':'data is null'}
        return result
    else:
        user={k:res[i] for i,k in enumerate(field)}
        return user



def update(table,field,data):
    conditions=["%s='%s'" % (k,data[k]) for k in data]
    sql="update %s set %s where id=%s " % (table,','.join(conditions),data['id'])
    cur.execute(sql)

