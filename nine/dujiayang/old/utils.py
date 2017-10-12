#!/usr/bin/env python                         
# _*_ coding: utf-8 _*_
import MySQLdb  as mysql
import config
import util

conn = mysql.connect(config.db_host,config.db_user,config.db_passwd,config.db_name,charset='utf8')
conn.autocommit(True) 
cur = conn.cursor()

def insert(table,field,data):
    sql = "insert into %s (%s) values (%s)"  % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
    res = cur.execute(sql)
    util.WriteLog('[utils.py-insert插入数据库]').info(sql) 
    if res:
        result = {'code':0,'msg':'insert ok'}
    else:
        result = {'code':1,'msg':'insert fail'}
    return result

def getlist(table,field):
    sql = "select * from %s" % table
    cur.execute(sql)
    util.WriteLog('[utils.py-getlist]').info(sql) 
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
    print sql
    cur.execute(sql)
    util.WriteLog('[utils.py-getone]').info(sql) 
    res = cur.fetchone()
    if res:
       user = {k:res[i] for i,k in enumerate(field)}
       result = {'code':0,'msg':user}
    else:
       result = {'code':1,'msg':"data is null"}
    return result


def update(table,field,data): 
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id=%s" %(table,','.join(conditions),data['id'])
    print sql
    res = cur.execute(sql)
    util.WriteLog('[utils.py-update]').info(sql) 
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result 

# 删除数据
def delete(table,uid):
        sql = "delete from %s where id = %s" % (table,uid)
        print "删除用户sql"
        print sql
        res = cur.execute(sql)
        if res:
                result = {'code':0,'msg':'delete ok'}
		util.WriteLog('[删除用户]').info('成功成功成功')
        else:
		util.WriteLog('[删除用户]').info('失败失败失败')
                result = {'code':1,'msg':'delete false'}
        print "util_delete_result"
        print result['msg']
        return result

   
