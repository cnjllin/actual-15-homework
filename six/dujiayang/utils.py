#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import MySQLdb as mysql

#db=mysql.connect('127.0.0.1','root','1234','reboot15',charset='utf8')
db=mysql.connect('121.43.191.76','reboot','reboot','reboot15',charset='utf8')
db.autocommit(True)
cur = db.cursor()

#注册
def insert(table,field,data):
	sql = "insert into %s(%s) values(%s)" % (table,','.join(field),','.join(['"%s"' % data[i] for i in field]))
	print "sql"
	print sql
	res = cur.execute(sql)
	print "res"
	print res
	if res:
		result = {"code":0,"msg":"insert ok"}
	else:
		result = {"code":1,"msg":"insert fail"}
	return result

#登录
def getone(table,field,data):
	if data.has_key("username"):
		sql = 'select %s from %s where username = "%s"' % (','.join(field),table,data["username"])
	else:
		sql = 'select %s from %s where id = "%s"' % (','.join(field),table,data["id"])
	print sql
	cur.execute(sql)
	res = cur.fetchone()
	print "fetchone"
	print res
	if res:
		user = {k:res[i] for i,k in enumerate(field)}
		print "enumerate"
		print user
		result = {"code":0,"msg":user}
	else:
		result = {'code':1,'msg':'data is null'}
	return result

#用户列表
def list(talbe,field):
	sql = "select * from %s" % table
	cur.execute(sql)
	res = cur.fetchall()
	if res:
		user = [{k:row[i] for i,k in emumerate(field)} for row in res]
		result = {'code':0,'msg':user}
	else:
		result = {'code':1,'errmsg':'data is null'}
	return result

#更新	
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
