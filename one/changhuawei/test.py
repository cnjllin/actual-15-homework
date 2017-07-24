#!/usr/bin/python
#coding:utf-8
#import hashlib
username = "chw"
userpasswd = "123"
#count = 0

name = raw_input("please input your name: ")
if name == username:
    print "welcom %s" % name
    while count <3:
        passd = raw_input("please your password: ")
        if passd == userpasswd:
            print "登录 成功,欢迎 {}".format(name)
            break
        else:
            print "密码 错误,请重试"
            count +=1
       

else:
    print "用户名 {} 不对，请重输 ".format(name)
