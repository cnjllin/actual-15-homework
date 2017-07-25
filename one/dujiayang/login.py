#!/usr/bin/python
#coding:utf-8
username='hehe'
realpwd = '123abc'
namecount = 1
count = 1
while namecount <=3:
	name = raw_input("输入用户名: ")
	if name != username:
		print "\033[41m用户名不存在\033[0m" 
	else:
		while count <= 3:
			if count == 3:
				print "\033[41m注意,你还有最后一次机会\033[0m"
			pwd = (raw_input("输入6位密码: "))
			if pwd == realpwd:
				print "\033[32m你好:%s,恭喜你已登录成功\033[0m" %name
				break
			pwd = list(pwd)
			pwdlen = len(pwd)
			if pwdlen != 6:
				print "\033[31m%s,你好,密码必须是6位,剩%s次机会\033[0m"%(name,3-count)
			else:
				print "\033[31m%s,你好,密码错误,剩%s次机会\033[0m"%(name,3-count)
			count+=1
			namecount+=1
	namecount+=1
