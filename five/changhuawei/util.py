#!/usr/bin/env python
#coding:utf-8

import MySQLdb as mysql
db = mysql.connect(host='127.0.0.1',user='root',passwd='123456',db='reboot15',port=3306,charset='utf8')
# db.autocommit(True)
cur = db.cursor()

def _reg(username,passwd,sex,age,phone,email,role):
    sql = "insert into user (username,password,sex,age,phone,email,role) values ('{}','{}','{}','{}','{}','{}','{}')".format(username,passwd,sex,age,phone,email,role)
    cur.execute(sql)
    db.autocommit(True)


# 登录
def _login(username,passwd):
    sql = "select * from user where username='{}' and password='{}'".format(username,passwd)
    cur.execute(sql)
    res = cur.fetchall()
    return res

# 查询all 
def chaxunall(): 
    sql = "select * from user"
    cur.execute(sql)
    res = cur.fetchall()
    # print res
    return res  
# 查询ID
def chaxunone(uid): 
    sql = "select * from user where id = '{}'".format(uid)
    cur.execute(sql)
    res = cur.fetchone()
    return res
# 修改
def _xiugai(username,password,sex,age,phone,email,role,uid):
    sql = "update user set username='{}',password='{}',sex='{}',age='{}',phone='{}',email='{}',role={} where id='{}'".format(username,password,sex,age,phone,email,role,uid)
    # print sql
    cur.execute(sql)
    db.autocommit(True)
# 删除
def _delete(uid):
    sql = "delete from user where id='{}'".format(uid)
    cur.execute(sql)
    db.autocommit(True)

