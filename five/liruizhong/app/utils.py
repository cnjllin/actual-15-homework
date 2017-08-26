#!/usr/bin/env python
#-*- coding:UTF-8 -*-

from db import DB

# 增加
def insert(username,password,sex,age,phone,email):
    role = 0
    db = DB()
    sql = "insert into user(username,password,sex,age,phone,email,role)values('%s','%s',%s,%s,'%s','%s',%s)"%(username,password,sex,age,phone,email,role)
    ret = db.insert(sql)
    return ret

# 删除
def delete(uid):
    db = DB()
    sql = "delete from user where id = %d" % uid
    ret = db.delete(sql)
    return ret

# 修改
def update(name,phone,passwd,uid):
    print name,phone,passwd,uid
    db = DB()
    sql = "update user set username='%s',phone='%s',password='%s' where id = %d" % (name,phone,passwd,uid)
    ret = db.update(sql)
    return ret

# 查询单条
def select(uid):
    db = DB()
    sql = "select * from user where id = %d" % uid
    ret = db.select(sql)
    return ret

# 查询全部
def select_all():
    db = DB()
    sql = "select * from user"
    ret = db.select(sql)
    return ret

# 根据name查询
def select_name(name):
    db = DB()
    sql = "select * from user where username = '%s'" % name
    ret = db.select(sql)
    return ret

# 判断注册用户信息
def judge_register_user(name,phone,passwd):
    user_name = name
    user_phone = phone
    user_passwd = passwd

    if user_name == "":
        error = "The user name cannot be empty"
        return error
    else:
        ret = select_name(user_name)
        if ret != ():
            error = "User already exists"
            return error
    if user_phone == "":
        error = "The phone number can't be empty"
        return error
    if len(user_phone) != 11:
        error = "Cell phone number error"
        return error
    if user_passwd == "":
        error = "The password cannot be empty"
        return error
    if len(user_passwd) <= 6:
        error = "The password number must be greater than 6 digits"
        return error
    else:
        error = ""
        return error

# 判断登录用户信息
def judge_login_user(name=None,passwd=None):
    user_name = name
    user_passwd = passwd
    ret = select_name(user_name)
    if ret != ():
        for i in ret:
            if user_name==i[1] and user_passwd==i[2]:
                #print "Login successful"
                return 0
            else:
                #print "The password is wrong"
                return 1

    else:
        error = "Users don't exist,Please register first"
        return error

