#!/usr/bin/python
#coding:utf-8
name = raw_input("请输入您的账号 :")
if name == "liaoxz":
	pas = raw_input("请输入您的账号密码 :")
 	if pas == "liaoxz":
	 print "欢迎登陆您的后台！"
	elif len(pas)<6:
	    print "请输入至少6位及6位以上的密码!"
	else:
	 print"请输入与名字匹配的密码"
elif len(name)<6:
 print "请输入的账号至少需要6位请检查后再次输入！"
else:
 print "请输入正确的姓名！"
