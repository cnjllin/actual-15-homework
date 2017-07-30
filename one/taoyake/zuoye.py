#!/usr/bin/python
#-*- coding:utf-8 -*-
#Author:taoyake
#date:2017-7-28

#导入隐藏不显示密码的模块
import getpass

username = 'taoyake'    #正确的登录用户名
password = '1234567'    #正确的登录密码,密码大于6位
count = 0               #计数器，默认为0

#通过user变量，获取到输入的用户名
user = raw_input("请输入您的用户名: ")

#如果countde值小于3,循环就会一直执行
while count < 3:
    if user != username:  #如果输入的用户不等于预先定义的用户名,则打印用户不存在并且退出循环
        print "对不起，你输入的%s用户不存在" % user
        break
    else:
        pwd = getpass.getpass("请输入您的密码: ")  #输入密码
        if pwd != password and len(pwd) <= 6:       #如果输入的密码连续三次小于六位数，则提示账号锁定并退出
            count = count + 1
            time = 3 - count
            if time == 0:
                print "密码输错三次，用户已经被锁定，请联系客服"
            else:
                print "您输入的密码太短，请输入超过六位的数字,您还有%d次机会" % time
                continue
        elif pwd != password:  #如果密码连续输错三次，提示账号锁定并退出
            count = count + 1
            time = 3 - count
            if time == 0:
                print "密码输错三次，用户已经被锁定，请联系客服"
            else:
                print "您输入的密码不正确,您还有%d次重试机会" % time
                continue
        else: #如果上边的都不成立，说明输入密码正确，提示登录成功
            print "恭喜您%s成功登录" % user
            break
