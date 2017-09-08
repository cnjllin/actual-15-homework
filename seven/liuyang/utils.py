#!/bin/env python
#coding=utf-8

import MySQLdb as mysql
conn=mysql.connect(host='127.0.0.1',user='root',passwd='piptest',db='liuyang',port=6666,charset='utf8')
conn.autocommit(True)
cur=conn.cursor()


def insert(table,field,user_dict):
	field = ['username','password','age','phone','email','role'] 
	sql = "insert into %s (%s) values (%s)"%(table,','.join(field),','.join(['"%s"' % user_dict[x] for x in field]))
	print sql
	res = cur.execute(sql)
	if res:
		result = {'code':0,'msg':'insert ok'}
	else:
		result = {'code':1,'msg':'insert fail'}
	return result


def getone(table,field,user_dict):
	if user_dict.has_key('username'):
		sql = 'select * from %s where username="%s";'%(table,user_dict['username'])
	else:
		sql = 'select * from %s where id ="%s"'%(table,user_dict['id'])
	print sql
	cur.execute(sql)
	res = cur.fetchone()
	if res:
		data = {k:res[i] for i,k in enumerate(field)}
		result = {'code':0,'msg':data}
	else:
		result = {'code':1,'msg':'data is null'}
	return result

def alllist(table,field):
	sql = 'select * from %s;'%(table)
	cur.execute(sql)
	res = cur.fetchall()
	if res:
		data = [{k:row[i] for i,k in enumerate(field)} for row in res]
		result = {'code':0,'msg':data}
	else:
		result={'code':1,'msg':'data is null'}
	return result

def modify(table,user_dict): 
    conditions = ["%s='%s'" % (k,user_dict[k]) for k in user_dict]
    sql = "update %s set %s where id=%s;" %(table,','.join(conditions),user_dict['id'])
    print sql 
    res = cur.execute(sql)
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result 

def deleteuser(table,user_dict):
	sql = 'delete from %s where id="%s";'%(table,user_dict['id'])
	res = cur.execute(sql)
	if res:
		result = {'code':0,'msg':'delete ok'}
	else:
		result = {'code':1,'msg':'data is null'}
	return result

cur.close
conn.close
