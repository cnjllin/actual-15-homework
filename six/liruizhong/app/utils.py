#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import MySQLdb as mysql
import MySQLdb.cursors

con = mysql.connect(
        host="localhost",
        port=3306,
        user="reboot",
        passwd="reboot@123",
        db="reboot15",
        charset="utf8",
        cursorclass = MySQLdb.cursors.DictCursor
    )

# 增加
def insert(sql):
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
        return True
    except:
        con.rollback()
        return False

# 删除
def delete(uid):
    cursor = con.cursor()
    sql = "delete from user where id = %d" % uid
    try:
        cursor.execute(sql)
        con.commit()
        return True
    except:
        con.rollback()
        return False

# 修改
def update(sql):
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
        return True
    except:
        con.rollback()
        return False

# 查询单条
def select(uid):
    cursor = con.cursor()
    sql = "select * from user where id = %d" % uid
    print sql
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
    except:
        print "数据异常!"
    return results

# 查询全部
def select_all():
    cursor = con.cursor()
    sql = "select * from user"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except:
        print "数据异常!"
    return results

# 根据name查询
def select_name(name):
    cursor = con.cursor()
    sql = "select * from user where username = '%s'" % name
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
    except:
        print "数据异常!"
    return results

# 判断注册用户信息
def judge_register_user(**kwargs):
    if kwargs['username'] == "":
        error = "The user name cannot be empty"
        return error
    else:
        ret = select_name(kwargs['username'])
        if ret != None:
            error = "User already exists"
            return error
    if kwargs['phone'] == "":
        error = "The phone number can't be empty"
        return error
    if len(kwargs['phone']) != 11:
        error = "Cell phone number error"
        return error
    if kwargs['password'] == "":
        error = "The password cannot be empty"
        return error
    if len(kwargs['password']) <= 6:
        error = "The password number must be greater than 6 digits"
        return error
    else:
        error = ""
        return error
# 判断登录用户信息
def judge_login_user(**info):
    user_name = info['name']
    user_passwd = info['passwd']
    ret = select_name(user_name)
    if ret != ():
        if user_name==ret['username'] and user_passwd==ret['password']:
            #print "Login successful"
            return 0
        else:
            #print "The password is wrong"
            return 1

    else:
        error = "Users don't exist,Please register first"
        return error

