#!/usr/bin/env python
# v2.0  Yujingming 20170726

#读取文件所有行，并存为字典
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
			print "恭喜你，登陆成功！"
			break
			
	