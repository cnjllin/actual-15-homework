#/usr/bin/python
#coding=utf-8
#定义usr_name usr_pwd初始值

'''
思路
1. 设定初始用户密码密码
2.判断用户名是否匹配 
if :
	3.定义输入密码次数，默认是0
	while:
	 	4.验证密码
		if:首先判断密码长度,如果小于6位，打印密码长度不够，重新输入
		if:再判断密码是否正确，
		else:
			密码不匹配，重新输入，剩余输入次数
	else:
		输入次数超过三次，账户锁定

else:

代码中涉及的知识
1.字符串格式化输入
print '%s'%(变量)
2.raw_input()函数获取用户输入
3.strip()函数，消除空格
4.len()判断字符串长度
'''
usr_name = 'liuyang'
usr_pwd = '123456'

user_name = raw_input('Please enter your user name：').strip()
# 判断用户是否存在，存在，则继续if中语句
if user_name == usr_name:
	count = 0
	# 判断输入次数，3次机会，输入错误超过3次，退出程序
	while count <3:
		user_pwd = raw_input('Please enter your user passwd: ').strip()
		# 判断密码长度，如果小于6,提示密码大于6位，重新输入，还有两次机会
		if len(user_pwd)<6:
			print '\033[1;31;40mPassword must be more than six,you have %s times,please input again！\033[0m'%(3-count)
		# 判断密码输入正确，打印欢迎
		if user_pwd == usr_pwd:
			print '\033[1;32;40mLogin sucessfully! \nHey %s,Welcome!\033[0m'%(user_name)
			break
		# 判断密码输入错误，并且输入次数不超过3次，打印密码输入错误，剩余输入次数
		else:
			print '\033[1;31;40mWrong password,you have %s times！\033[0m'%(3-count)			
		count += 1
	# 判断输入次数超过3次，打印密码连续输入错误三次，账户锁定
	else:
		print '\033[1;31;40mUser name or password wrong input more than three times, the account will be locked!!!\033[0m'
# 判断用户名不存在，打印用户不存在
else:
	print 'Sorry,user %s not exists,please confirm!'%(user_name)

