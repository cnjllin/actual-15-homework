#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/8/15日07点47分

import gconf

# 获取用户所有信息函数
def GetUser():
    user_list = []
    f = open(gconf.USER_FILE, 'r')
    for user in f:
        if not user:
            break
        line = user.strip('\n').split(':')
        user_list.append(line)
    return user_list

# 用户登录验证函数
def ValidateLogin(username, password):
    _all_user = GetUser()
    for user in _all_user:
        if username == user[0] and password == user[2]:
            return True
    return False

# 用户注册验证函数
def ValidateFind(username):
    _all_user = GetUser()
    for user in _all_user:
        if username == user[0]:
            return True
    return False

# 用户注册函数
def UserAdd(username, age, password):
    try:
        f = open(gconf.USER_FILE, 'a+')
        f.write("%s:%s:%s\n" % (username, age, password))
        f.close()
        return True
    except:
        return False


if __name__ == '__main__':
    # 用户注册验证测试
    username = 'nick'
    # print ValidateFind(username)

    # 用户注册测试
    username = 'nick1'
    age      = 23
    password = '123123'
    # print UserAdd(username,age,password)

    # 用户登录测试
    username = 'wd'
    password = '123'
    # print ValidateLogin(username,password)

    # 获取所有用户测试
    # print GetUser()