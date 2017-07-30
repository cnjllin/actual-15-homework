#!/usr/bin/env python
# coding: utf-8

dict1 = {'username': 'reboot', 'password': '12345678'}
x = raw_input("UserName:")

if x == dict1['username']:
	for i in range(3):
		p = raw_input("Password:")
		if len(p) >6 and p == dict1['password']:
			print "登录成功"
			break
		elif i == 2 and p != dict1['password']:
			print "用户已锁定"
			break
		else:
			print "密码错误"
			continue

else:
    print '用户不存在'
