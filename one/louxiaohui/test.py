#!/usr/bin/python
# -*- coding:utf-8 -*-

for i in range(0,4):
    name = raw_input("请输入用户名:")
    password = raw_input("输入密码:")
    if name == "wd":
        if password == "123":
            print "欢迎,%s,登入成功" % name
        else:
            print "密码错误"        
    else:
        print "用户名%s不存在" % name
    if i > 1 :
	print "you have input wrong username more than 3 times"
        break
    print i

