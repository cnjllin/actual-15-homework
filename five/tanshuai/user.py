#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/8/15日07点47分
import dbutils

# 获取用户所有信息函数
def GetUser(sql=''):
    count, users = dbutils.execute_sql(sql)
    return users

# 用户登录验证函数
def ValidateLogin(username, password):
    sql = 'select * from user where username=%s and password=%s'
    count, rt_list = dbutils.execute_sql(sql, args=(username, password))
    return count != 0

# 验证用户是否存在
def ValidateUser(username):
    sql = 'select * from user where username=%s'
    count, rt_list = dbutils.execute_sql(sql, args=(username,))
    print count
    return count != 0

# 添加用户函数
def UserAdd(*args):
    sql = "insert into user(username,password,sex,age,phone,email,role) values(%s,%s,%s,%s,%s,%s,%s)"
    count, rt_list = dbutils.execute_sql(sql=sql, args=args[0], fetch=False)
    print count
    return count != 0

# 更新用户函数
def UserUpdate(*args):
    sql = "update user set password=%s,sex=%s,age=%s,phone=%s,email=%s,role=%s where id=%s"
    count, rt_list = dbutils.execute_sql(sql=sql, args=args[0], fetch=False)
    print count
    return count != 0

# 删除用户函数
def UserDelete(uid):
    sql = 'delete from user where id=%s'
    count, rt_list = dbutils.execute_sql(sql, uid, fetch=False)
    return count != 0

if __name__ == '__main__':


    # 添加用户测试
    args = ('谭帅03','123456',1,27,'18512341234','185@185.com',1)
    # print UserAdd(args)

    # 更新用户测试
    args = ('谭帥06','123456',1,27,'18512341234','185@185.com',1,44) #最后位置是ID
    # print UserUpdate(args)

    # 用户登录验证测试
    username = '谭帥06'
    password = '123456'
    # print ValidateLogin(username, password)

    # 获取所有用户测试
    sql = "select * from user"
    # print GetUser(sql=sql)

    # 删除用户测试
    # uid = (44,)
    # print UserDelete(uid)

    # 添加用户验证测试
    username = '谭帅03'
    # print ValidateUser(username)
