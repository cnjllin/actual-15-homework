#!/usr/bin/env python
#_*_ codind: utf-8 _*_

import MySQLdb as mysql

#db=mysql.connect('127.0.0.1','root','1234','reboot15',charset='utf8')
db=mysql.connect('121.43.191.76','reroot','reboot','reboot15',charset='utf8')
db.autocommint(True)
cur = db.cursor()

#注册
def insert(table,field,data):
	sql = "insert into %s(%s) values(%s)" % (table,','.join(field),','.join(['"%s"' % data[i] for i in field]))
	print sql
	try:
	res = cur.execute(sql)
		result = {"code":0,"msg":"insert ok"}
	except :
		result = {"code":1,"msg":"insert fail"}
	return result
	
#登录
def getone(table,field,data):
	if data.has_key("username"):
		sql = 'select * from %s where username = "%s"' % (table,data["username"]) 
	else:
		sql = 'select * from %s where id = "%s"' % (table,data["id"])
	print sql
	cur.execute(sql)
	res = cur.fetchone()
	if res:
		user = {k:res[i] for i,k in enumerate(field)}
		print user
		result = {"code":0,"msg":user}
	else:
		result = {'code':1,'msg':'data is null'}
	return result
















	
