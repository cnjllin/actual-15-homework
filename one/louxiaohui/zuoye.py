#!/usr/bin/python
# -*- coding:utf-8 -*-

count = 1
num = 10
total =3
user="test"
password="123456"

name = raw_input("please input your name:").strip()
if name == user:
    while count <=3:
        total=total-1
        count+=1
        input_pass = raw_input("please input password:").strip()
        if len(input_pass) < 6:
            print "密码少于6位，你还有%d次机会" % total
            break
        if input_pass == password:
            print "输入正确"
            break
        else:
            print "密码输入错误,你还有%d次机会" % total
    else:
        print "输入错误超过三次，退出"
else:
    print "%s用户不存在" % name
