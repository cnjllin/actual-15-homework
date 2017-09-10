#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,redirect,render_template,session
from utils import insert,getone
import json

app= Flask(__name__)
app.secret_key="dfsdfdfsdfsfsfdfdfsdf"

field = ["id","username","password","role"]

@app.route('/')
@app.route('/index/')
def index():
#	if not session:
#		return redirect('/login/')
#	print session
	username = "wd"
	return render_template("index.html",username=username)

@app.route('/reg/',methods=['POST','GET'])
def reg():
	if request.method == "POST":
		data = {k:v[0].strip() for k,v in dict(request.form).iteritems()}	
		print data
		field = ["username","password","role"]
		info = insert('dujiayang',field,data)
		print info
		print data["role"]
		if info['code'] == 0:
			return render_template("register.html",data=data)
			#return redirect('/login/')
		else:
			return render_template("register.html",view=info)
	return render_template('register.html')

@app.route('/login/',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		data = {k:v[0].strip() for k,v in dict(request.form).iteritems()}
		print "data"
		print data
		info = getone('dujiayang',field,data)
		print "info"
		print info
		if info["code"] == 0:
			if info["msg"]["password"] == data["password"]:
				session['username'] = data['username']
				session['role'] = info['msg']['role']
				print "session"
				print session
				return render_template("login.html",view=info)
			else:
				error = "u password is fail"
				return render_template("login.html",view=error)
		else:
			return render_template("login.html",view=info)
	return render_template("login.html")

#用户列表
@app.route("/userlist/")
def userlist():
	if not session:
		return redirect("/login")
	result = getlist('user',field)
	if result['code'] == 0:	
		result = result['msg']
	return render_template('userlist.html',result=result,info=session)

#用户信息
@app.route('/userinfo/')
def userinfo():
	if not session:
		return redirect("/login/")
	uid = request.args.get('id',"")
	print uid
	data = {'id':uid}
	result = getone('user',field,data)
	print result
	if result['code'] == 0:
		result = result['msg']
#	return json.dumps(result)
	return render_template('update.html',result=result)

#用户更新
@app.route('/update/')	
def modify():
	if request.method == 'POST':
		data = dict(request.form)
		data = {k:v[0] for k,v in data.items()}
        	result = update('user',field,data)
        	if result['code']==0:
			return redirect("/userlist/")
	else:
		return render_template('update.html',result=result)
		
		

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
