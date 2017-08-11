#/usr/bin/python
#coding=utf-8
#注册登录函数


#获取用户密码文件并生成dict
def userfile():
	temp_dict = {}
	with open('user_passwd.txt','a+') as f:
		for line in f:
			user_name = line.strip('\n').split(':')[0]
			user_pwd = line.strip('\n').split(':')[1]
			temp_dict[user_name]=user_pwd
	#返回用户密码字典，登录或注册是判断用户是否存在字典中
	return temp_dict

#注册系统
def registor():
	with open('user_passwd.txt','a+') as f:
		user_dict = userfile()
		#print user_dict
		count = 0
		while count <3:
			#输入用户名
			user_name = raw_input('请输入用户名：').strip()
			#print user_name
			#判断用户名是否存在于userfile函数生成的字典中,如果存在，注册提示用户已存在
			if user_name in user_dict:
				print "用户已存在，请重新输入"
			elif user_name == ' ':
				print '用名输入不能为空'
			else:
				#输入密码判断两次输入是否匹配
				user_pwd = raw_input('输入密码： ')
				re_pwd = raw_input('请确认密码： ')
				if user_pwd == re_pwd:
					print '%s用户注册成功！'%(user_name)
					f.write('%s:%s\n'%(user_name,user_pwd))
					break
				else:
					print '两次密码不匹配，请重新输入！'
		else:
			print '输入错误超过三次'

#登录系统
def login():
	#调用userfile()函数生成字典，判断用户密码
	user_dict = userfile()
	#登录
	count = 0
	while count <3:
		name = raw_input('输入用户名： ')
		if name in user_dict:
			pwd = raw_input('输入密码： ')
			if pwd == user_dict[name]:
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
    	act = '选择输入错误'
    return act

#执行选择登录或者注册
result = choose()
print result

