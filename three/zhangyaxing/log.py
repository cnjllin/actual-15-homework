#/usr/bin/env python
#coding:utf-8


def log_up():
	while True:
		name = raw_input('请输入姓名：').strip()
		if len(name) == 0:
			print '用户名不能为空'
			break
		else:
			password = raw_input('请输入密码:').strip()
			repass = raw_input('请再次输入:').strip()
			if len(password)==0 or password!=repass:
				print '密码输入错误'
				continue
			else:
				f =open('user.txt','a+')
				f.write('%s:%s\n'%(name,password))
				f.close()
				print '注册成功'
				break

def log_in():
	name = raw_input('请输入姓名：').strip()
	if len(name) == 0:
		print '用户名不能为空'
	else:
		f =open('user.txt','r+')
		for line in f.readlines():
			li = line.strip()
			username = li.split(':')[0]
			password = li.split(':')[1]
			if name != username:
				# print '用户不存在'
				# break
				continue
			else:
				passwd = raw_input('请输入密码：')
				if passwd != password:
					print '密码错误'
					break
				else:
					print '登陆成功'
					break
	f.close()

if __name__ == '__main__':
	log = raw_input('login or logup?').strip()
	if log == 'login':
		log_in()
	elif log == 'logup':
		log_up()
	else:
		print '请重新输入'








