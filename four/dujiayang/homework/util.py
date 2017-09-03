#!/usr/bin/env python
#coding:utf-8

#name = 'test1'
#password = '100'

##注册用户函数
def register(name,password):
#	user_list = [] 
	user_dict = {}
	with open('user.txt','r') as file:
		f = file.readlines()
		for i in f:
			user_dict[i.strip('\n').split(':')[0]] = i.strip('\n').split(':')[1]   ##为字典赋值
#			user_list.append(i.strip('\n').split(':'))
#	print user_dict
	if user_dict.has_key(name):                   ##判断用户在不在字典里
		return "%s already exist" % name
	else:
		file = open('user.txt','a+')
		file.write("%s:%s\n" % (name,password))
		file.close()
		
#register(name,password)


##登录函数
def login(name,password):
        user_dict = {}
        with open('user.txt','r') as file:
                f = file.readlines()
                for i in f:
                        user_dict[i.strip('\n').split(':')[0]] = i.strip('\n').split(':')[1]   ##为字典赋值
	print user_dict
	if user_dict.has_key(name):
		if password == user_dict[name]:
			return "%s  login ok" %name
		else:
			return "the %s passwd is error" %name
	else:
		return "the name is error"
#res = login('gsan','123')
#res = login(name,password)
#print res
