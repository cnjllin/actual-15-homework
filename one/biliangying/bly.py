#! /usr/bin/python
#coding:utf-8
i = 1
name=raw_input("Please input your name:")
if name=="hehe":
	while i <= 3:
		i =i+1
		a = 4-i
		password=raw_input("Please input your passsword:")
		if len(password) < 6:
			print "密码不得小于6位数,还有 %s 次机会" % a
		elif password != "123456":
			print "密码错误,还有 %s 次机会" % a
		else:	
			print "Welcome!"
			break
else:
	print "用户名错误"
