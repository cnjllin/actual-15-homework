#!/usr/bin/env python
#coding:utf8

from flask import Flask,request,redirect,render_template
from utils import insert,getone
app= Flask(__name__)

field = ["username","password","role","id"]

@app.route('/')
@app.route('/index/')
def index():
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
		if result['code'] == 0:
			#return render_template("register.html",data=data,result=result)
			return redirect('/login/')
		else:
			return render_template("register.html",result=result)
	return render_template('register.html')

@app.route('/login/',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		data = {k:v[0].strip() for k,v in dict(request.form).iteritems()}
		print data
		info = getone('dujiayang',field,data)
		print info
		if result["role"] == 0 and result["msg"]["password"] == data["password"]:
			return render_template("login.html",view=result)
		else:
			return render_template("login.html",view=result)
	return render_template("login.html")
		
		

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
