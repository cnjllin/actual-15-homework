#!/usr/bin/python
# -*- coding:utf-8 -*-
# **********************************************************
# * Author        : louxiaohui
# * Email         : 1031138448@qq.com
# * Last modified : 2017-08-19 20:31
# * Filename      : mysql_connect.py
# * Description   : 
import MySQLdb as mysql
import sys
conn = mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

query = "0,'test', password('2a3456'), 0, 18, '1888888888', 'test02@qq.com', 0"
sql1 = "insert into user values(%s)" %query
sql = "select * from user"
username = 'test01'
passwd = '123456'
sql2 = "select * from user where username = '%s' and password = password('%s')" %(username,passwd)
username = 'test05'
passwd = '987654'
sex = 0
age = 18
phone = '13967341234'
email = 'test05@qq.com'
role = 0
sql3 = "select * from user where username = '%s' and password = password('%s')" %(username,passwd)
print sql3
value = "'%s', password('%s'), %s, %s, '%s', '%s', %s" %(username,passwd,sex,age,phone,email,role)
print value

user_info_list=['username','password','sex','age','phone','email','role']
user_info = ",".join(user_info_list)
sql4 = "insert into user(%s) values (%s)" %(user_info,value)
print sql4

try:
    cur.execute(sql1)
except Exception as e:
    print 'err : %s' %e
cur.execute(sql2)
#cur.execute(sql2,(username,passwd))
cur.execute(sql4)
cur.execute(sql)
s = cur.fetchall()

for i in s:
    print i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]
