#!/usr/bin/python
#coding:utf-8
def login():
	fo = open("/root/actual-15-homework/three/chenfei/config/user.txt")
	# 读取所有，并将存为字典
	users = {}
	# 将文件结果存为列表
	content = fo.readlines()
	fo.close()
	#print content
	for user in content:
		name = user.rstrip("\n").split(":")[0]
		users[name]=user.rstrip("\n").split(":")[1]
	print users

	# 判断用户的账户密码，都ok提示登录成功，否则失败
	count = 0
	while True:
		count +=1
		if count >3:
		   print "对不起，输入错误，账号已经锁定"
		   break;
		name = raw_input("请输入姓名:").strip()
		if name not in users:
			print "用户不存在，请重新输入"
			continue;
		else:
			 password = raw_input("请输入密码:").strip()
			 if password != users[name]:
				print "密码输入有误"
				continue;
			 else:
				  print "恭喜你,登录成功"
				  break;
