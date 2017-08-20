#!/usr/bin/env python
# -*- coding: utf-8 -*-

#获取所有用户和密码信息模块
def GetUser():
    user_list = []
    f = open("userinfo.txt", 'r')
    for user in f:
        if not user:
            break
        line = user.strip('\n').split(':')
        user_list.append(line)
    return user_list  #返回所有用户名和密码组成的一个list


# 用户登录验证函数
def UserLogin(username, password):
    all_user = GetUser()
    for user in all_user:
        print user[0],user[1]
        if username == user[0] and password == user[1]:
            return True
    return False

# 用户注册验证函数
def CheckUser(username):
    all_user = GetUser()
    for user in all_user:
        if username == user[0]:
            return True
    return False
