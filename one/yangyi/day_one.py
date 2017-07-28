#!/usr/bin/pyton
#coding:utf-8

'''作业：实现用户名密码的登录验证
   1:判断用户名密码是否正确，正确则打印欢迎信息，错误则输出具体错误原因信息
   2:用户可以连续输入三次密码。超过三次则锁定用户
   3:密码位数必须超过6位
'''
#name = 'TailorYang'
#password = '123456'
import sys
time = 0
name = raw_input('Please input your username :')
while time < 3 :
	if name.strip().lower()== 'tailoryang':
		password = raw_input('please input your password :')
		if password == '123456':
			print 'Sign in successfully, welcome %s'%(name)
			break
		elif len(password) < 6:
			print 'The password must be longer than six digits,remaining times %s !'%(2-time)
			time += 1
		else:
			print 'Wrong password, please re-enter,remaining times %s !'%(2-time)
			time +=1
	else :
		print 'This user not exit !'
		sys.exit()
else :
	print 'Your chance is running out!'
	sys.exit()