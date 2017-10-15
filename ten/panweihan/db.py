#!/usr/bin/python 
# -*- coding:utf-8 -*-

import MySQLdb as mysql

import config

import utils

import traceback

db = mysql.connect(host=config.host, user=config.user, passwd=config.passwd, db=config.db, port=config.port, charset=config.charset)
cur = db.cursor()
db.autocommit(True)

# 解决中文编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time

# 日志文件路径
info_filename = "E:/Reboot15/homework/nine/tmp/info.log"
error_filename = "E:/Reboot15/homework/nine/tmp/error.log"




# 增加数据
def insert(table, field, data):
    sql = "insert into %s (%s) values(%s)" % (table, ','.join(field), ','.join(['"%s"' % data[x] for x in field]))
    try:
        res = cur.execute(sql)
        utils.WriteLog("db模块", info_filename).info("执行语句：%s" %sql)
        result = {'code': 0, 'msg': 'insert ok'}
    except:
        result = {'code': 1, 'errmsg': 'insert fail'}
        utils.WriteLog("db模块", error_filename).error("执行语句：%s,错误信息：%s" %(sql, traceback.format_exc()))
    return result


# 删除一条数据
def delete(table,data):
    sql = "delete from %s where id = %s" %(table,data['id'])
    try:
        res = cur.execute(sql)
        utils.WriteLog("db模块", info_filename).info("执行语句：%s" %sql)
        result = {'code': 0, 'msg': 'delete ok'}
    except:
        result = {'code': 1, 'errmsg': 'delete fail'}
        utils.WriteLog("db模块", error_filename).error("执行语句：%s,错误信息：%s" %(sql, traceback.format_exc()))
    return result


# 修改数据库
def updata(table,data):
    conditions = ["%s = '%s'" %(k, data[k]) for k in data]
    sql = "update %s set %s where id = %s" %(table,",".join(conditions),data['id'])
    try:
        res = cur.execute(sql)
        result = {'code': 0, 'msg': 'updata ok'}
        utils.WriteLog("db模块", info_filename).info("执行语句：%s" %sql)
    except:
        result = {'code': 1, 'errmsg': 'updata fail'}
        utils.WriteLog("db模块", error_filename).error("执行语句：%s,错误信息：%s" %(sql, traceback.format_exc()))
    return result


# 查看所有数据
def getlist(table, field):
    sql = "select * from %s" % table
    try:
        cur.execute(sql)
        res = cur.fetchall()
        user = [{k: row[i] for i, k in enumerate(field)} for row in res]
        result = {'code': 0, 'msg': user}
        utils.WriteLog("db模块", info_filename).info("执行语句：%s" %sql)
    except:
        result = {'code': 1, 'errmsg': 'data is null'}
        utils.WriteLog("db模块", error_filename).error("执行语句：%s,错误信息：%s" %(sql, traceback.format_exc()))
        result = result['msg']
    return result


# 查看一条数据
def getone(table, field, data):
    if data.has_key('username'):
        sql = 'select * from %s where username = "%s"' %(table, data["username"])
    elif data.has_key('name'):
        sql = 'select * from %s where name = "%s"' %(table, data["name"])
    else:
        sql = 'select * from %s where id = "%s"' %(table, data["id"])
    try:
        cur.execute(sql)
        res = cur.fetchone()
        user = {k:res[i] for i, k in enumerate(field)}
        result = {'code': 0, 'msg': user}
        utils.WriteLog("db模块", info_filename).info("执行语句：%s" %sql)
    except:
        result = {'code': 1, 'errmsg': 'data is null'}
        utils.WriteLog("db模块", error_filename).error("执行语句：%s,错误信息：%s" %(sql, traceback.format_exc()))
    return result