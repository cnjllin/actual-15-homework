#!/usr/bin/env python
# -*- coding: utf-8 -*-
a=1
while a <=3:
    name = raw_input("请输入用户名：")
    passwd = raw_input("请输入密码：")
    if name == "liyx":
        if len(passwd) > 6:
            if passwd == "1234567":
                print "登录成功！欢迎您 %s" % (name)
                break
            else:
                print "密码错误，请重新输入,剩余%s次机会" % (3-a)
                a=a+1
        else:
            print "密码位数必须超过6位,请重新输入,剩余%s次机会" % (3-a)
            a=a+1
    else:
        print "没有%s这个用户,请重新输入，剩余%s次机会" % (name,3-a)
        a=a+1
else:
    print "byes"
