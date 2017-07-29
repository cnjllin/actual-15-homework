#!/usr/bin/python
#coding:utf-8
count = 1
name = raw_input("请输入你的账户名称：")
if name == "liaoxz":
 while count <=3:
     count = count + 1
     num = 4 - count
     psd = raw_input("请输入账户密码：")
     if psd == "liaoxz":
      print "{}欢迎登录您的后台".format(name)
      break
     elif len(psd)<6:
      print "密码必须在6位以上"
     else :
      print "密码错误,还有 {} 次机会,当你密码输入次数达到限制，账户将被锁定".format(num)

else:
 print "您输入的账号不存在！"
