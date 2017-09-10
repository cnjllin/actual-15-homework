#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import MySQLdb as mysql

#db=mysql.connect('127.0.0.1','root','1234','reboot15',charset='utf8')
db=mysql.connect('121.43.191.76','reboot','reboot','reboot15',charset='utf8')
db.autocommit(True)
cur = db.cursor()

sql = "select * from dujiayang;"
cur.execute(sql)
res = cur.fetchall()
print "fetchall---res"
print res
print '\n'
field = ["id","username","password","role"]
user = [{k:row[i] for i,k in enumerate(field)} for row in res]
print "enumerate"
print user
#用户列表
#def list(talbe,field):
#	sql = "select * from %s" % table
#	cur.execute(sql)
#	#res = cur.fetchall()
#	if res:
#		user = [{k:row[i] for i,k in emumerate(field)} for row in res]
#		result = {'code':0,'msg':user}
#	else:
#		result = {'code':1,'errmsg':'data is null'}
#	return result
