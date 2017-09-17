#!/usr/bin/python 
# -*- coding:utf-8 -*-

import MySQLdb as mysql

db = mysql.connect(host="127.0.0.1", user="root", passwd="123456", db="reboot15", port=3306, charset='utf8')
cur = db.cursor()
db.autocommit(True)

# 解决中文编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 增加用户
def insert(table, field, data):
    sql = "insert into %s (%s) values(%s)" % (table, ','.join(field), ','.join(['"%s"' % data[x] for x in field]))
    res = cur.execute(sql)
    if res:
        result = {'code': 0, 'msg': 'insert ok'}
    else:
        result = {'code': 1, 'errmsg': 'insert fail'}
    return result


# 删除一条数据
def delete(table,data):
    sql = "delete from %s where id = %s" %(table,data['id'])
    res = cur.execute(sql)
    if res:
        result = {'code': 0, 'msg': 'delete ok'}
    else:
        result = {'code': 1, 'errmsg': 'delete fail'}
    return result


# 修改数据库
def updata(table,data):
    conditions = ["%s = '%s'" %(k, data[k]) for k in data]
    sql = "update %s set %s where id = %s" %(table,",".join(conditions),data['id'])
    res = cur.execute(sql)
    if res:
        result = {'code': 0, 'msg': 'updata ok'}
    else:
        result = {'code': 1, 'errmsg': 'updata fail'}
    return result


# 查看所有数据
def getlist(table, field):
    sql = "select * from %s" % table
    cur.execute(sql)
    res = cur.fetchall()
    if res:
        user = [{k: row[i] for i, k in enumerate(field)} for row in res]
        result = {'code': 0, 'msg': user}
    else:
        result = {'code': 1, 'errmsg': 'data is null'}
    result = result['msg']
    return result


# 查看一条数据
def getone(table, field, data):
    if data.has_key('username'):
        sql = 'select * from %s where username = "%s"' %(table, data["username"])
    else:
        sql = 'select * from %s where id = "%s"' %(table, data["id"])
    cur.execute(sql)
    res = cur.fetchone()
    if res:
        user = {k:res[i] for i, k in enumerate(field)}
        result = {'code': 0, 'msg': user}
    else:
        result = {'code': 1, 'errmsg': 'data is null'}
    return result