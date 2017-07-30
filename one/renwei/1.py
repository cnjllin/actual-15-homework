#!/usr/bin/python 
# -*- coding: utf-8 -* 
name=raw_input("pleases input your name : ")
password=raw_input("pleases input your password : ")
if name != 'baihui':
   print '您输入用户不存在，退出登录!!!'
elif name == 'baihui' and password == '123':
   print '欢迎您登录成功!!!i'
elif name == 'baihui' and password != '123' :
   print '您的密码错误，请继续输入密码!!!'
