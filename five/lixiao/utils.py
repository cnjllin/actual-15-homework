#!/usr/bin/python
#coding:utf-8

from flask import Flask,request,render_template,redirect

import MySQLdb as mysql
con=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot15',port=3306,charset='utf8')
con.autocommit(True)
cur = con.cursor()

#查询数据库
def search():
    cur.execute('select * from user')
    res = cur.fetchall()
    return res

#根据用户名查询

def search_user():
    cur.execute('select * from user where username = "%s"' %username)
    res = cur.fetchall()
    return res

#根据id查询
def search_id():
    cur.execute('select * from user where username = "%s"' %id)
    res = cur.fetchall()
    return res
'''
#用户登录
def login(username,passwd):
    res = search_user()
    for user in db_res:
        if (username == user[1] and passwd == user[2]):
            return '0'
        elif (username == user[1] and user[7] == 0):
            return '1'
        else:
            return '2'

#用户注册
def reg_user(username,passwd,repasswd):
    user_list = []
    res = search()
    for user in db_user:
        user_list.append(user[1])
        if username not in user_list:
            if (len(passwd) > 6 or passwd == repasswd):
                return '0'
            else:
                return '1'
        else:
            return '2'
'''
#数据库写入数据
def add_db():
     cur.execute('insert into user (username,password,sex,age,phone,email,role) values ("%s","%s","%s",""%s,"%s","%s","%s")' %(username,passwd,sex,age,phone,email,role))
     #con.commit()
     return 0


#用户修改
def update():
    cur.execute('update user set password="%s",sex="%s",age="%s",phone="%s",email="%s",role="%s"'%(passwd,sex,age,phone,email,role))
    return 0

#删除用户
def dele(id):
    cur.execute('delete from user where id = "%s"' %id)
    return 0
