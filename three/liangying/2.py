#!/usr/bin/python
#coding:utf-8
#用户注册登陆
#注册
def register():
	f = open('a.txt','a+')
	a = []
	while True:
		for i in f.readlines():
       			a.append(i.split(':')[0])
       		name=raw_input('用户名:').strip()
       		if len(name)==0:
               		print '用户名不能为空'
               		break
		elif name in a:
               		print '用户存在'
               		break
       		else:
               		passwd1=raw_input('密码:').strip()
               		passwd2=raw_input('请再次输入密码:').strip()
       		if passwd1 != passwd2 or len(passwd1)==0:
               		print '密码错误'
               		break
       		else:
                	f.write("%s:%s\n" % (name,passwd1))
               		f.close()
               		print '注册成功'
			break
#登陆
def Login():
	f=open('a.txt')
	a=[]
	b={}
	for i in f.readlines():
        	a.append(i.strip('\n').split(':'))
	for j in a:
        	b[j[0]]=j[1]
	name = raw_input("用户名:")
	if name in b.keys():
		passwd = raw_input("密码:")
        	if passwd == b[name]:
                	print 'welcome'
        	else:
                	print '密码错误'
	else:
        	print '用户名不存在'
def start():
	action = raw_input('input action:register/Login:')
	if action == "register":
		res=register()
	elif action == 'Login':
		res = Login()
	return res
	print res
x = start()
print x
