# coding: utf-8
import sys


# 用户登录函数
def UserLogin():
	us = raw_input("请输入用户名:").strip()
	f = open('user.txt', 'r')
	us_list = f.read().split(":")
	if us != us_list[0]:
	    res =  '用户名不存在'
	else:
	    ps = raw_input("请输入密码:").strip()
	    if ps != us_list[1]:
	        res =  '密码错误!'
	    else:
	        res =  '登录成功！'
	f.close()
	return res


# 用户注册函数
def UserRegister():
	us = raw_input("请输入用户名:")
	ps = raw_input("请输入密码:")
	f = open('user.txt', 'w+')
	f.write("%s:%s" % (us, ps))
	f.close()
	return '注册成功！用户名:%s 密码:%s'% (us, ps)


# 入口函数
def start():
	print '(0) 登录'
	print '(1) 注册'
	action = raw_input('请输入数字来进行操作：').strip()

	if action != '0' and action != '1':
		print '非法输入'
		sys.exit() 
	if action == '0':
		res = UserLogin()
	else:
		res = UserRegister()
	return res

print start()