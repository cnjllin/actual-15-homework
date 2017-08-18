#!/bin/env python
#coding=utf-8

'''
项目需要分析：

通过flask实现注册登录
 模块拆解：1.注册，返回注册成功，通过get前端获取到的用户名、密码，写入用户密码文件
 		   2.登录，返回注册成功，依然是通过前端获取的用户名密码与用户密码文件匹配判断返回

登录是单独的页面，表单
注册是单独的页面，表单

'''

from flask import Flask,render_template,request

app = Flask(__name__)

#获取用户密码并存入字典
def userfile():
	temp_dict = {}
	with open('user.txt','a+') as f:
		for line in f:
			user_name = line.strip('\n').split(':')[0]
			user_pwd = line.strip('\n').split(':')[1]
			temp_dict[user_name]=user_pwd
	#返回用户密码字典，登录或注册是判断用户是否存在字典中
	return temp_dict

#index页显示登录页面
@app.route('/')
def index():
	return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
	user_dict = userfile()
	if request.method == "POST":
		name = request.form.get('username')
		passwd = request.form.get('passwd')
		if name in user_dict:
			if passwd == user_dict[name]:
				status = 'Login sucessfully!'
			else:
				status = 'Wrong passwd,please confirm!'
		else:
			status = 'User %s not exist!'%(name)
	return render_template('loginsucess.html',status=status)	

#注册页面
#访问URL:http://192.168.30.76:9999/registor
#通过request获取到不定传入的参数，并将后端获取的数据渲染结果返回resuccess.html展示出来
@app.route('/registor')
def registor():
	return render_template('registor.html')
#注册页面
@app.route('/reg',methods=['POST','GET'])
def reg():
	user_dict = userfile()
	#print user_dict
	if request.method=="POST":
		name = request.form.get('username')
		passwd = request.form.get('passwd')
		repwd = request.form.get('repwd')
		print name,passwd,repwd
		if name not in user_dict:
			if passwd == repwd:
				status = 'User %s registor sucessfully!'%(name)
				with open('user.txt','a+') as f:
					f.write('%s:%s\n'%(name,passwd))
			else:
				status = 'Password does not match!'
		else:
			status = 'User %s exsits!'%(name)
	 	#return render_template('registor.html',name=name)
		return render_template('regsucess.html',name=name,status=status)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9999,debug=True)




