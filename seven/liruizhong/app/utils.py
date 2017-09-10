#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb as mysql

conn = mysql.connect('localhost','reboot','reboot@123',db='reboot15',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

# 插入数据
def insert(table,field,data):
    sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'insert ok'}
    else:
        result = {'code':1,'msg':'insert fail'}
    return result

# 查询数据
def getone(table,field,data):
    if data.has_key('username'):
        sql = 'select * from %s where username = "%s"' % (table,data['username'])
    else:
        sql = 'select * from %s where id = "%s"' % (table,data['id'])
    cur.execute(sql)
    res = cur.fetchone()
    if res:
        user = {k:res[i] for i,k in enumerate(field)}
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'msg':'data is null'}
    return result

# 查询全部
def listall(table,field):
    sql = "select %s from %s" % (','.join(field),table)
    cur.execute(sql)
    res = cur.fetchall()
    if res:
        user = [{k:row[i] for i,k in enumerate(field)} for row in res]
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'msg':'data is null'}
    return result

# 更新数据
def updateuser(table,field,data):
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id = %s" % (table,','.join(conditions),data['id'])
    print sql
    res = cur.execute(sql)
    if res != 0:
        result = {'code':0,'msg':'update success'}
    else:
        result = {'code':1,'msg':'update false'}
    return result

# 删除数据
def delete(table,uid):
    sql = "delete from %s where id = %s" % (table,uid)
    res = cur.execute(sql)
    if res != 0:
        result = {'code':0,'msg':'delete success'}
    else:
        result = {'code':1,'msg':'delete false'}
    return result
