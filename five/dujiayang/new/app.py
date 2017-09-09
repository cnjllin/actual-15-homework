#!/usr/bin/env python
#coding:utf-8

from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
#import sys
#sys.setdefaultencoding('utf8')
app = Flask(__name__)


# 首页
@app.route('/')
@app.route('/index/')
def index():
        username = "wd"
        return render_template("index.html",username=username)
# 注册页
@app.route('/reg/',methods=['GET','POST'])
def reg():
	info = {}
	if request.method == 'POST':
		print dict(request.form)
		username = request.form.get('username',"")
		passwd = request.form.get('passwd',"")
		role = request.form.get('role',1)
		info = {"name":username,"passwd":passwd,"role":role}
		if username == "123" or passwd == "":
			error = "username exist or passwd can not null"
			#error = "用户已存在或密码不能为空"	
			return render_template("register.html",error=error)
		return render_template("register.html",info=info)
	return render_template("register.html",info=info)
		


# 登录页


# 管理页

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
