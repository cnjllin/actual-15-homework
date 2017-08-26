#!/usr/bin/env python 
# File Name: run.py
# Author: luofeng
# Mail: 18210085737@139.com 
# Blog: https://www.liyanlan.com 
# _*_ coding: utf-8 _*_

from flask import Flask, request, render_template, redirect
from utils import * 
app = Flask(__name__)

@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/register/",methods=['GET','POST'])
def register():
	if request.method == 'POST':
		username = request.form.get('fullname')
		phone = request.form.get('phone_num')
		password = request.form.get('password')
		if user_regis(username) == 1:
			return redirect("/register/")
		else:
			db_insert(username,phone,password)
			return redirect("/login/")

	return render_template("regis.html") 

@app.route("/login/",methods=['GET','POST'])
def login():
	if request.method == 'POST':
		phone = request.form.get('account')
		password = request.form.get('password')
		if user_login(phone,password) == 1:
			return redirect("/userlist/")
		else:
			return redirect("/register/")

	return render_template("login.html")

@app.route("/userlist/")
def userlist():
	ret = db_select_all()
	return render_template("userlist.html",data=ret)

@app.route("/delete/")
def delete():
	uid = request.args.get('uid')
	db_delete(uid)
	return redirect("/userlist/")

@app.route("/update/",methods=['GET','POST'])
def update():
	if request.method == 'GET':
		uid = request.args.get('uid')
		return render_template('update.html')
	elif request.method == 'POST':
		uid = request.form.get('uid')
		username = request.form.get('username')
		password = request.form.get('password')
		sex = request.form.get('sex')
		age = request.form.get('age')
		phone = request.form.get('phone_num')
		email = request.form.get('email')
		role = request.form.get('role')
		db_update(username,password,sex,age,phone,email,role,uid)
		return redirect("/userlist/")

	return render_template('login.html') 

if __name__ == "__main__":
 app.run(
 host="0.0.0.0",
 port=8080,
 debug=True)
