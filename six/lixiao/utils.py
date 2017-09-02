#!/usr/bin/python
#coding:utf-8

#0 -->sucess; 1-->fail  2 -->null
from flask import Flask,request,render_template,redirect

import MySQLdb as mysql
con=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot15',port=3306,charset='utf8')
con.autocommit(True)
cur = con.cursor()

#查询数据库所有数据
def user_list(user,field):
    cur.execute('select * from %s' %user)
    res = cur.fetchall()
    user = [{k:row[i] for i,k in enumerate(field)} for row in res]
    return user

#根据id查询单用户
def user_id(user,field,uid):
    cur.execute('select * from %s where id = "%s"' %(user,uid))
    res = cur.fetchone()
    user = {k:res[i] for i,k in enumerate(field)}
    return user

#根据username查询单用户
def user_name(user,field,username):
    cur.execute('select * from %s where username = "%s"' %(user,username))
    res = cur.fetchone()
    return res

#插入数据
def insert(user,field,data):
    sql = 'insert into %s(%s) values(%s)' %(user,",".join(field),",".join(['"%s"' %v for i,v in data.items()]))
    res = cur.execute(sql)
    return res

#删除数据
def dele(user,uid):
    sql = 'delete from %s where id = %s' %(user,uid)
    res = cur.execute(sql)
    return res

#修改数据
def update(user,field,data):
   sql = 'update %s set %s where id = "%s"' %(user,','.join(['%s="%s"' %(i,v) for i,v in data.items()]),data['id'])
   res = cur.execute(sql)
   return res

