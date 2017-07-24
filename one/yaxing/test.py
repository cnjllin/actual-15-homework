#usr/bin/nev/python
# -*- coding=utf-8 -*-

#username=raw_input("please input your name:")
count=1
while count<=3:
	username=raw_input("please input your name:")
	password=int(raw_input("please input your password:"))
	if username=="yaxing":
		if password==1234567:
			print "欢迎"
			break
		elif len(str(password))<7:
			print "您的密码小于7位"
			count+=1
		else:
			print "您的密码错误"
			count+=1			
	else:
		print "用户名不存在"
		count+=1