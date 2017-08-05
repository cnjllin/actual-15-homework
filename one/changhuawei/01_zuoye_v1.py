#!/usr/bin/env python
#encoding: utf-8
#name:changhuawei 
#eml:513314416@qq.com
#time:201707232200
'''
实现用户名密码登陆验证
1：判断用户名密码是否正确，正确则打印欢迎信息，错误则输出具体错误原因信息
2：用户可以连续输入三次密码。超过三次则锁定用户
3：密码位数必须超过6位
'''
####
import sys
username = "chw"
usrpasswd = "1234567"
count = 0
time = 3
name = raw_input("请输入用户名: ").strip()
if name == username:
    while count < 3:
        passwd = raw_input("请输入密码: ").strip()
        if len(passwd) < 6:
            print "密码错误，要大于6位"
            break
        elif passwd == usrpasswd:
            print "欢迎 {} !".format(name)
            break
        else:
            time -=1
            count +=1
            print "密码错误，请重试.还有{}次机会".format(time)
    else:
        print "对不起，3次机会用完，账户 {} 被锁定".format(time)
else:
    print "用户名 {} 错误,请重试".format(name)
