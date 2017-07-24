#/usr/bin/python
#coding=utf-8

#实现用户名密码登陆验证
# 1：判断用户名密码是否正确，正确则打印欢迎信息，错误则输出具体错误原因信息
# 2：用户可以连续输入三次密码。超过三次则锁定用户
# 3：密码位数必须超过6位

# 格式：\033[显示方式;前景色;背景色m
#   说明:
#
#   前景色            背景色            颜色
#   ---------------------------------------
#     30                40              黑色
#     31                41              红色
#     32                42              绿色
#     33                43              黃色
#     34                44              蓝色
#     35                45              紫红色
#     36                46              青蓝色
#     37                47              白色
#
#   显示方式           意义
#   -------------------------
#      0           终端默认设置
#      1             高亮显示
#      4            使用下划线
#      5              闪烁
#      7             反白显示
#      8              不可见
#
#   例子：
#   \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
#   \033[0m          <!--采用终端默认设置，即取消颜色设置-->]]]

#思路 关键信息
#用户名 密码（必须超过6位）3次验证，返回具体错误信息，超过三次锁定用户

user_name = raw_input('Please enter your user name：')

if user_name == 'liuyang':
	count = 0
	while count <=3:
		user_pwd = raw_input('Please enter your user passwd: ')
		if user_pwd == '':
			print '\033[1;31;40mPassword cannt be empty,please input again！\033[0m'
		elif len(user_pwd)< 6:
			print '\033[1;31;40mPassword must be more than six,please input again！\033[0m'
		else:
			print '\033[1;32;40mLogin sucessfully! \nHey %s,Welcome!\033[0m'%(user_name)
			break
		count += 1
	else:
		print '\033[1;31;40mUser name or password wrong input more than three times, the account will be locked!!!\033[0m'
else:
	print 'Sorry,user %s not exists,please confirm!'%(user_name)

