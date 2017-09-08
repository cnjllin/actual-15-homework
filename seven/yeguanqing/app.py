#!/usr/bin/env python
#coding:utf-8

from flask import Flask,render_template,request,redirect,session
from utils import insert,getone,list,update,delete
import json

app = Flask(__name__)
app.secret_key="dfkafkasdkfsak"

field = ['id','username','password','role']

# 首页函数
@app.route('/') 
@app.route('/index') 
def index():
#	if not session:
#		return redirect("/login/")
	return render_template("userlist.html")


# 注册函数
@app.route('/reg/',methods=['GET','POST'])
def reg():
	#user = {}
	if request.method == 'POST':
		#user = dict((k,v[0]) for k,v in dict(request.form).items())
		user = {k:v[0] for k,v in dict(request.form).items()}
		print user
		field = ['username','password','role']
		result = insert('user2',field,user)
		if result['code'] == 0:
			return redirect("/login/")
		else:
			return render_template("reg.html", result=result)	
	return render_template("reg.html")


# 登陆函数
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).items()}
		result = getone('user2',field,data)
		if result['code'] == 0:
			if result['msg']['password'] == data['password']:
				session['username'] = data['password']
				session['role'] = result['msg']['role']
				if session['role'] ==0:
					return redirect('/userlist/')
				else:
					return redirect("/")
			else:
				result['errmsg'] = "user is exist, password is wrong."
		else:
			result['errmsg'] = "user is not exist"
			return  render_template("login.html",result=result)
	return render_template("login.html")


# 登出函数
@app.route('/logout/')
def logout():
	if session:
		session.clear()
	return redirect("/login/")



# 用户列表
@app.route('/userlist/')	
def userlist():
	result = list('user2',field)
	if result['code'] == 0:
		result = result['msg']
	return render_template("userlist.html",result=result)



# 用户信息
@app.route('/userinfo/')
def userinfo():
	uid = request.args.get('id',"")
	data = {'id':uid}
	result = getone('user2',field,data)
	if result['code'] == 0:
		result = result['msg']
	#return json.dumps(result)
	return render_template("update.html",result=result)


# 更新函数
@app.route('/update/',methods=['GET','POST'])
def modity():
	if request.method == 'POST':
        	data = dict(request.form)
        	data = {k:v[0] for k,v in data.items()}
       		result = update('user2',field,data)
        	if result['code']==0:
               		return redirect("/userlist/")
      	        else:
                 	return render_template('update.html',result=result)

# 删除函数
@app.route('/delete/')
def delid():
	if request.method == 'GET':
		uid = int(request.args.get('id'))
		result = delete('user2',uid)
		if result['code']==0:
			return redirect("/userlist/")
		else:
			return result

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=1234,debug=True)
