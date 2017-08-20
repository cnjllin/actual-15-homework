#!/usr/bin/python
#coding:utf-8
import shelve
import string
import random
datafile = 'userinfo.db'

# 保存用户注册的数据
def save_userinfo(name, password, age, job, tel, email):
    database = shelve.open(datafile)
    userinfo = database.get('userinfo',[])
    userinfo.insert(0,{'name':name,'password':password,'age':age,'job':job,'tel':tel,'email':email})
    database['userinfo'] = userinfo
    database.close()

# 检查注册时用户合法性
def user_ifexits(name):
    database = shelve.open(datafile)
    if 'userinfo' not in database:
        userinfo = []
        database['userinfo'] = userinfo
    else:
        userinfo = database['userinfo']
    users = [i['name'] for i in database['userinfo']]
    for i in name:
        if i not in string.letters + '0123456789' + '_':
            return 'invalid username!'

    if name in users:
        return 'the username exits!'
    else:
        return 'ok'

# 检查注册时密码合法性
def passwd_valid(password1, password2):
    if len(password1) < 6:
        return 'password is too short!'
    else:
        if password1 != password2:
            return 'password mismatch!'
        return 'ok'

# 用户注册
def user_register(name, password1, password2):
    if user_ifexits(name) == passwd_valid(password1, password2):
        return 'registered successfully'
    else:
        if user_ifexits(name) != 'ok':
            return user_ifexits(name)
        else:
            return passwd_valid(password1, password2)

# 显示登录后用户信息
def user_info(name):
    database = shelve.open(datafile)
    for i in database['userinfo']:
        if i['name'] == name:
            users_info = i.copy()
            del users_info['password']
            break
    return users_info

# 用户登录
def login(name,password):
    database = shelve.open(datafile)
    users_pass = {i['name']:i['password'] for i in database['userinfo']}
    if name in users_pass:
        if password == users_pass[name]:
            return "login successfully"
        else:
            return "incorrect password!"
    else:
        return "invalid username!"

if __name__ == '__main__':
    pass
