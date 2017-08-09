#!/usr/bin/env python
#encoding: utf-8
#name:changhuawei 
#eml:513314416@qq.com

def zhuce():
	return "欢迎注册"
def login():
	return "欢迎登陆"
def staus():
	data = raw_input("plrase input zhuce/login: ").strip()
	if data == 'zhuce':
		res = zhuce
	elif data == 'login':
		res = login
	else:
		res = '错误,请重试'
	return res
print staus()
