#!/usr/bin/env python
#-*- coding:utf-8 -*-

#-----------------------------------
#     FileName: CMDB.py
#         Desc:
#       Author: copy
#      Version:
#     CreatTime: 2017-09-02
# ----------------------------------
# 
import MySQLdb as mysql

conn=mysql.connect(host="127.0.0.1",user="root",passwd="",db="reboot15",port=3306,charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

def insert(table,field,data):
    sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' %data[x] for x in field]))
    print sql
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'insert ok'}
    else:
        result = {'cide':1,'msg':'insert failed'}
    return result

def getone(table,field,data):
    if data.has_key('username'):
        sql = 'select * from %s where username = "%s"' % (table,data['username'])
    else:
        sql = 'select * from %s where id="%s"' % (table,data['id'])
    print sql
    cur.execute(sql)
    res = cur.fetchone()
    if res:
        user = {k:res[i] for i,k in enumerate(field)}
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'msg':'data is null'}
    return result


def getlist(table,field):
    sql = "select * from %s" % table
    cur.execute(sql)
    res = cur.fetchall()
    if res:
       user = [{k:row[i] for i,k in enumerate(field)} for row in res]
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
    
def delete(table,user_dict):
	sql = 'delete from %s where id="%s";'%(table,user_dict['id'])
	res = cur.execute(sql)
	if res:
		result = {'code':0,'msg':'delete ok'}
	else:
		result = {'code':1,'msg':'data is null'}
	return result