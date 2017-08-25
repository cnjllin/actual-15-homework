#!/usr/bin/env python
#coding:utf-8
'''
登录用户注册请求，将前端HTML表单里的数据获取到，然后处理存入文件
'''


from flask import Flask,request,render_template,redirect

app = Flask(__name__)

# 定义一个函数user_exist判断用户在注册的时候是否存在
def user_exist(username):
	with open('user_info.txt','rb') as user_info:
		flag = 1
		for line3 in user_info.readlines():
			user, passwd = line3.strip().split(':')
			if username == user:
				flag = 0
		return flag

# 定义登陆路由，获取POST提交的两个参数，判断用户名和密码是否正确
@app.route('/login/',methods=['POST', 'GET'])

def login():
	if request.method == "POST":
		username = request.form.get('username')
		passwd = request.form.get('passwd')
		with open('user_info.txt','r') as user_info:
			userlist = []
			for line1 in user_info:
				list01 =  line1.strip().split(':')
				userlist.append((list01[0],list01[1]))
			for line2 in userlist:
				if line2[0] ==username and line2[1] == passwd:
					return 'Hello %s, welcome to login.' % username
				else:
					return  'username or password is wrong, please try again.'
	return  render_template('login.html')

# 定义注册路由，获取POST注册的三个参数，用户名和双重密码的输入，并调用用户是否存在的函数，将前端HTML(表单)里的数据通过POST方式获取到，然后处理存入文件。
@app.route('/register/', methods=['POST','GET'])

def register():
	if request.method == 'POST':
		username = request.form.get('username')
		if user_exist(username) == 0:
			return "sorry, %s user already exists." % username
		else:
			passwd = request.form.get('passwd')
			repasswd = request.form.get('passwd')
			if passwd == repasswd:
				with open('user_info.txt','a+') as user_info:
					user_info.write("%s:%s \n" % (username,passwd))
				return redirect("/login/")
	return render_template('register.html')
if __name__ =='__main__':
	app.run(host='0.0.0.0', port=8888,debug=True)
