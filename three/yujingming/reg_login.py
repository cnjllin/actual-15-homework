#!/usr/bin/env python
# v2.0  Yujingming 20170726
def reg():
	f =open('data.txt','a+')
	while True: 
		name = raw_input("Please input the name:").strip()
		if len(name) == 0:
			print "User not exist, please input again:"
			break #
		else:
			password = raw_input("Please input the pwd:").strip()
			repass = raw_input("Please input the pwd:").strip()
			if len(password)==0 or password !=repass:
				print "pwd wrong"
				continue #
			else:
				f.write("%s:%s\n" % (name,password))
				f.close()
				return "欢迎注册"
				break



def login():
	f1= open('data.txt','a+')
	users ={}
	content =f1.readlines() #将文件结果存为列表
	f1.close()

	#输出content
	for user in content:
		name=user.rstrip('\n').split(':')[0]
		users[name]=user.rstrip('\n').split(':')[1]
	print users

	#判断用户账号密码，如果都OK 提示登陆成功，否则Fail
	count=0
	while True:
		count +=1
		if count>3:
			print "对不起，输入错误超过3次，账户已经锁定，请联系管理员："
			break
		name=raw_input("请输入姓名：").strip()
		if name not in users:
			print "用户不存在，请重新输入："
			continue
		else:
			password =raw_input("请输入密码：").strip()
			if password != users[name]:
				print "密码输入有误"
				continue
			else:
				return "欢迎登录"
				break

	

def start():
	action = raw_input("请输入reg/login:").strip()

	if action == "reg":
		res = reg()
	else:
		res = login()
	return res


result = start()
print result


