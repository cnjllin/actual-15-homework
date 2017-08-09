#/usr/bin/python
#coding=utf-8
#注册登录函数

#注册系统
def registor(name,pwd,re_pwd):
	with open('user_passwd.txt','a+') as f :
	#判断密码是否为空
			if name == '':
				print '用户名不能为空，请重新输入！'
			else:
			 	if pwd == re_pwd:
					print '用户%s注册成功！'%(name)
					f.write('%s:%s\n'%(name,pwd))
				else:
					print '密码不匹配，请重新输入！'


#登录系统
def login(name,pwd):
	temp_dict = {}
	with open('user_passwd.txt','a+') as f:
		for line in f:
			user_name = line.strip('\n').split(':')[0]
			user_pwd = line.strip('\n').split(':')[1]
			temp_dict[user_name]=user_pwd
			#print temp_dict
		#登录判断用户名是否存在：
		if name in temp_dict:
			#print temp_dict[name]
			#输入密码
			if pwd == temp_dict[name]:
				print '用户%s登录成功'%(name)
			else:
				print '密码输入错误'
		else:
			print '用户不存在，请确认！'

#登录或者注册
def choose():
    action =raw_input('input a action:registor/login ').strip()

    if action == 'registor':
        name = raw_input('输入用户名: ').strip()
        pwd = raw_input('输入密码: ').strip()
        re_pwd =raw_input('再次输入密码: ').strip()
        act = registor(name,pwd,re_pwd)
    elif action =='login':
    	name = raw_input('输入用户名: ').strip()
        pwd = raw_input('输入密码: ').strip()
        act= login(name,pwd)
    else:
    	print '选择输入错误'
    return act

#执行选择登录或者注册
result = choose()
