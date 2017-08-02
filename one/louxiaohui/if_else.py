#!/usr/bin/python
# -*- coding:utf-8 -*-
name = raw_input("please input your name:")
password = raw_input("please input your password:")
if name == "wd":
    if password == "123":
        print "恭喜,%s,登陆成功" % name
    else:
        print "密码错误"	    
else:
    print "%s用户不存在" % name
