#!/usr/bin/python
#coding:utf-8
#name:娄旭
#time:2017-7-24
import sys
count=1
times=3
while count <= 3:
    name=raw_input('please input you name:')
    password=raw_input('please input you password:')
    if name == 'louxu' and password == '123456':
        print "登录成功"
        sys.exit(0)
    elif password != '123456':
        print "您的密码不正确"
    count=count + 1
    times=times - 1
    print "\033[33m还有%d次输入机会！！！\033[33m"%(times)
    if count == 4:
        print "三次输入均不正确，您的账号将被锁定一天！！！" 
