#!/usr/bin/env python
#_*_ codind: utf-8 _*_

import MySQLdb as mysql

#db=mysql.connect('127.0.0.1','root','1234','reboot15',charset='utf8')
db=mysql.connect('121.43.191.76','reboot','reboot','reboot15',charset='utf8')
db.autocommit(True)
cur = db.cursor()

def insert(table,field,data):
	sql = "insert into %s(%s) values(%s)" % (table,','.join(field),','.join(['"%s"' % data[i] for i in field]))
	print sql
	res = cur.execute(sql)
	if res:
		result = {"code":0,"msg":"insert ok"}
	else:
		result = {"code":1,"msg":"insert fail"}
	return result
	
