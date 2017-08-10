#/usr/bin/python
#coding=utf-8
#注册登录函数

#注册系统
def registor():
	with open('user_passwd.txt','a+') as f :
		count = 0
		while count <3:
			user_name = raw_input('请输入用户名：')
			if user_name == ' ':
			    print '用户名不能为空，请重新输入！'
		 	else:
				user_pwd = raw_input('输入密码： ')
				re_pwd = raw_input('请确认密码： ')
				if user_pwd == re_pwd:
					print '%s用户注册成功！'%(user_name)
					f.write('%s:%s\n'%(user_name,user_pwd))
					break
				else:
					print '两次密码不匹配，请重新输入！'
				count += 1
		else:
			print '输入错误超过三次'


#登录系统
def login():
	temp_dict = {}
	with open('user_passwd.txt','a+') as f:
		for line in f:
			user_name = line.strip('\n').split(':')[0]
			user_pwd = line.strip('\n').split(':')[1]
			temp_dict[user_name]=user_pwd
		#print user_passwd_dict
		#登录
		count = 0
		while count <3:
			name = raw_input('输入用户名： ')
			if name in temp_dict:
				pwd = raw_input('输入密码： ')
				if pwd == temp_dict[name]:
					print '登录成功'
					break
				else:
					print '密码输入错误'
				
			else:
				print '用户不存在，请确认！'	
			count += 1
		else:
			print '输入错误超过3次'

#登录或者注册
def choose():
    action =raw_input('input a action:registor/login ').strip()

    if action == 'registor':
        act = registor()
    elif action == 'login':
        act = login()
    else:
    	print '选择输入错误'
    return act

#执行选择登录或者注册
result = choose()
