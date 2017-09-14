#!/usr/bin/python
# -*- coding:utf-8 -*-
# **********************************************************
# * Author        : louxiaohui
# * Email         : 1031138448@qq.com
# * Last modified : 2017-08-28 04:24
# * Filename      : mysql.py
# * Description   : 
# * ********************************************************
import MySQLdb as mysql
import config
import hashlib
conn = mysql.connect(
        host = config.host ,
        user = config.user,
        passwd = config.passwd,
        db = config.db,
        port = config.port,
        charset = config.charset)
# set autocommit to True to enable the insert happened successfully
conn.autocommit(True)
# create a cursor
cur = conn.cursor()

field = ['id','username','password','role']

def insert(table,field,data):
    sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
    print sql
    try:
        res = cur.execute(sql)
        if res:
            result = {'code':0,'msg':'insert ok'}
        else:
            result = {'code':1,'msg':'insert fail'}
    except Exception as e:
        result = {'code':1,'msg':'insert fail'}
    return result

def getone(table,field,data):
    if data.has_key("username"):
        sql = "select * from %s where username = '%s'" % (table,data['username'])
    else:
        sql = "select * from %s where id = '%s'" %(table,data['id'])
    print sql
    cur.execute(sql)
    res = cur.fetchone()
    if res:
        user = {k:res[i] for i,k in enumerate(field)}
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'msg':"data is null"}
    return result

def user_list(table,field):
    sql = "select * from %s" % table
    cur.execute(sql)
    res = cur.fetchall()
    if res:
        user = [{k:row[i] for i,k in enumerate(field)} for row in res]
        print user
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'errmsg':'data is null'}
    return result

def update(table,field,data): 
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id=%s" %(table,','.join(conditions),data['id'])
    print sql 
    res = cur.execute(sql)
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result 

def delete(table,data):
    id = data['id']
    sql = 'delete from %s where id = %s' % (table,id)
    print sql 
    res = cur.execute(sql)
    print res
    if res :
        result = {'code':0,'msg':'delete ok'}
    else:
        result = {'code':1,'errmsg':'delete fail'}
    return result 
