#!/bin/env python
#coding:utf8
# Author:liuyang
# create time:2017/8/17

from flask import Flask,request,render_template,redirect,session
from utils import *
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')

app=Flask(__name__)
app.secret_key="daf"

field = ['id','username','password','age','phone','email','role'] 

# 主页面
@app.route('/')
@app.route('/index/')
def index():
	print session
	if not session:
		return redirect('/login')
	return render_template('base.html')

# 用户注册
@app.route('/registor/',methods=['POST','GET'])
def registor():
	if request.method == 'POST':
		user_dict = {k:v[0] for k,v in dict(request.form).items()}
		print user_dict
		result = insert('user',field,user_dict)
		if result['code'] == 0:
			return redirect('/login/')
		else:
			return render_template('registor.html',result=result)
	return render_template('registor.html')

# 用户登录
@app.route('/login/',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		user_dict = {k:v[0] for k,v in dict(request.form).items()}
		print user_dict
		result = getone('user',field,user_dict)
		print result
		if result['code'] ==0:
			session['username'] = user_dict['username']
			session['role'] = result['msg']['role']
			print session
		else:
			result['errmsg']="user not exist"
		return json.dumps(result)
	return render_template('login.html')

# 用户登录界面,普通用户只能看到个人信息，管理员可以看到用户列表
@app.route('/user/')
def user():
    if not session:
	return render_template('login.html')
    username=session['username']
    user_dict={'username':username}
    result=getone('user',field,user_dict)
    print result
    #return json.dumps(data)
    return render_template('index.html',res=session ,result=result['msg'])

# 管理员用户界面 
@app.route('/userlist/')
def userlist():
	if not session:
		return redirect('/')
	result = alllist('user',field)
	print result
	return render_template('userlist.html',result=result)

# 显示用户个人信息
@app.route('/userinfo/')
def userinfo():
	if not session:
		return redirect('/login/')
	uid = request.args.get('id')
	user_dict = {'id':uid}
	result = getone('user',field,user_dict)
	print result
	if result['code'] == 0:
		result = result['msg']
	#return json.dumps(result)
		return json.dumps(result)

# 更改用户信息
@app.route('/update/',methods=['POST','GET'])
def update():
	if not session:
		return redirect('/login')
	if request.method == 'POST':
		#data = dict(request.form)
		user_dict = {k:v[0] for k,v in dict(request.form).items()}
		print user_dict
		result = modify('user',user_dict)
		return json.dumps(result)
		#if result['code']==0:
			#return redirect("/userlist/")
		#else:
			#result = result['errmsg']
			#return render_template('update.html',result=result)

# 删除用户
@app.route('/delete/')
def delete():
	if not session:
		return redirect('/login')
	uid = request.args.get('id')
	user_dict = {'id':uid}
	result = deleteuser('user',user_dict)
	print result
	return json.dumps(result)
	#if result['code'] == 0:
	#	return redirect('/userlist/')

# 增加用户信息
@app.route('/adduser/',methods=['GET','POST'])
def adduser():
	if request.method == 'POST':
		user_dict = {k:v[0] for k,v in dict(request.form).items()}
		print user_dict
		result = insert('user',field,user_dict)
		if result['code'] == 0:
			return json.dumps(result)
	#		result['errmsg']="user not exist"
	return render_template('add.html')

# 登出系统
@app.route('/logout/')
def logout():
	session.clear()
	return redirect('/login')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8888,debug=True)

