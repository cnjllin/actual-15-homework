#! /usr/bin/python
#__*__ conding: UTF-8 __*__

import gconf

#获取用户所有信息
def GetUser():
    user_list = []
    f = open(gconf.USER_FILE, 'r')
    for user in f:
        if not user:
            break
        line = user.strip('\n').split(':')
        user_list.append(line)
     return user_list

#用户登录验证函数

def Validatelogin(username,password):
    _all_user = GetUser()
    for user in _all_user:
        if username == user[0] and password == user[2]:
            return True
    return False

#用户注册验证函数

def ValidateFind(username):
    _all_user = GetUser()
    for user in _all_user:
        if username == user[0]:
             return True
    return False

#用户注册函数
def UserAdd(username,age,password):
    try:
       f = open(gconf.USER_FILE, 'a+')
       f.write("%s:%s:%s"\n % (username,age,password))
       f.close()
    except:
        return False


if __name__ == '__main__':
    #用户注册验证测试
    username = 'cf'
    print ValidateFind(username)
 
    #用户注册测试
    username = 'cf'
    age      = 21
    password = '123'
    print UserAdd(username,age,password)


   #用户登录测试
   username = 'kk'
   password = '123'
   print Validatelogin(username,password)

