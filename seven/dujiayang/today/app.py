#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from utils import insert,getone,listall,updateuser,delete
import json

app = Flask(__name__)
app.secret_key="abcdefhehehaha"

field = ['id','username','password','role']

# 首页
@app.route('/')
@app.route('/index/')
def index():
	#if not session:
	#	return redirect('/login/')
	#return redirect('/userinfo/')
	return render_template('index.html')
# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).items()}
		field = ['username','password','role']
		result = insert('user1',field,data)
		if result['code'] == 0:
			return redirect('/login/')
		else:
			return render_template('register.html',result=result)
	return render_template('register.html')

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).iteritems()}
		result = getone('user1',field,data)
		if result['code'] == 0:
			if result['msg']['password'] == data['password']:
				session['username'] = data['username']
				session['role'] = result['msg']['role']
				print "session"
				print session
				if session['role'] == 0:
					return redirect('/userlist/')
				else:
					return redirect('/userinfo/')
			else:
				result = 'code0 password is fail'
				print result
				return render_template('login.html',result=result)	
		else:
			result = 'code1 user is not exist'
			print result
			return render_template('login.html',result=result)
	return render_template('login.html')

# common用户信息
@app.route('/userinfo/')
def userinfo():
	if not session:
		return redirect('/login/')
	data = {'username':session['username']}	
	result = getone('user1',field,data)
	if result['code'] == 0:
		result = result['msg']
		return render_template('userinfo.html',result=result)
	return render_template('userinfo.html',result=result)
	

# 用户列表,admin才能看
@app.route('/userlist/')
def userlist():
	if not session or session['role'] == 1:
		return redirect('/login/')
	result = listall('user1',field)
	print "app_userlist_result"
	print result
	ret = result['msg']
	print ret
	if result['code'] == 0:
		return render_template('userlist.html',result=result['msg'])
	return render_template('userlist.html',result=result)

# 更新
@app.route('/update/',methods=['GET','POST'])
def update():
	if not session:
		return redirect('/login/')
	if request.method == 'GET':
		data = {}
		data['id'] = int(request.args.get('id'))
		print data
		result = getone('user1',field,data) 
		print result
		if result['code'] == 0:
			return render_template('update.html',result=result['msg']) 	
	if request.method == 'POST':
		data = {k:v[0].strip() for k,v in dict(request.form).iteritems()}
		result = updateuser('user1',field,data)
		print "post result"
		print result
		if result['code'] == 0 and session['role'] == 0:
			return redirect('/userlist/')
		elif result['code'] == 0 and session['role'] == 1:
			return redirect('/userinfo/')
		else:
			return render_template('update.html',result=result)

# 删除用户
@app.route('/delete/')
def delete_user():
	if not session:
		return redirect('/login/')
	uid = int(request.args.get('id'))
	result = delete('user1',uid)
	if result['code'] == 0 and session['role'] == 0:
		return redirect('/userlist/')
	elif result['code'] == 0 and session['role'] == 1:
		return redirect('/userinfo/')
	else:
		result = "user is nulled"
		return redirect('/userinfo/',result=result)

# 销毁session
@app.route('/logout/')
def logout():
	session.clear()
	return redirect('/index/')

if __name__ == '__main__':
	app.run(host='59.110.12.72',port=9999,debug=True)
