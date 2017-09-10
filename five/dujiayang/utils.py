#!/user/bin/env python
#coding:utf-8
import MySQLdb as mysql
db = mysql.connect(host="121.43.191.76",user='reboot',passwd='reboot',db='reboot15',port=3306,charset='utf8')
db.autocommit(True)
cur = db.cursor()
#注册：
def signin((id=null,username,passwd,sex=null,age=null,phone=null,email=null,role=1)):
	sql = 'insert into dujiayang values(id,username,passwd,sex,age,phone,email,role)'
	cur.execute(sql)
