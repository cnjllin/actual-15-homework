#!/usr/bin/env python
#encoding: utf-8
#name:changhuawei 
#eml:513314416@qq.com
#time:201708091700
import sys
#用户注册模块
def zhuce():
	#打开文件追加方式
	f = open('yonghu.txt','a+')
	#获取输入用户
	username = raw_input("请输入用户名: ").strip()
	while True:
		#获取并确认密码一致，打印成功
	    passwd = raw_input("请设置密码: ").strip()
	    passwd1 = raw_input("请确认密码: ").strip()
	    if passwd == passwd1:
	        #print "注册用户{}成功".format(username)
	        return "注册用户{}成功".format(username)
	        break
	    else:
	    	#print "请重试"
	    	return "请重试"
	    sys.exit()
	aa = "{}:{}\n".format(username,passwd)
	#写入用户名密码到文件
	f.write(aa)
	f.close()
#登录模块
def login():
	data = {}
	#获取用户密码，定义到data字典
	with open('yonghu.txt') as f: 
		for line in f:
			users = line.rstrip().split(":")
			data[users[0]] = users[-1]
	#获取用户输入
	name1 = raw_input("plrase input your name: ").strip()
	pass1 = raw_input("plrase input your pass: ").strip()
	#判断用户在不在data，并判断密码
	if name1 in data:
		if pass1 == data[name1]:
		    #print '欢迎登陆{}'.format(name1)
		    return '欢迎登陆{}'.format(name1)
		else:
			#print 'passwd err'
			return 'passwd err'
	else:
		#print 'name err'
		return 'name err'

def status():
	data = raw_input("plrase input  zhuce/login:  ").strip()
	if data == 'zhuce':
		request = zhuce()
	elif data == 'login':
		request = login()
	else:
		request = 'input err'
	return request
print status()

