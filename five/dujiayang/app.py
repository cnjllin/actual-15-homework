#!/usr/bin/env python
#coding:utf-8

import requests,redirect,render_template
import Flask from flask
import MySQLdb as mysql
import utils

app = Flask(__name__)
db = mysql.connect(host="121.43.191.76",user='reboot',passwd='reboot',db='reboot15',port=3306,charset='utf8')
db.autocommit(True)
cur = db.cursor()

@app.route('/',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		passwd = request.form.get('passwd')
		sql = 'select * from dujiayang where username = %s and password = %s' %(username,passwd) ##查看库里有没有用户和密码
		if cur.execute(sql):
			hello = "welcom to my page"
			sql = 'select * from dujiayang where username = %s' %username
			cur.execute(sql)
			res = cur.fetchone()
			print res
			return redirect('ok.html',hello=hello,res=res)       #到ok页面
			
		else:
			error = '用户名或密码错误,please check'
			return render_template('login.html',error=error)
	return render_template('login.html')

@app.route('/reg/',methods=['GET','POST'])
def reg():
	if request.method == 'POST':
		username = request.form.get('username') 
		passwd = request.form.get('password')
		cpasswd = request.form.get('cpassword')
		sex = request.form.get('sex')
		age = request.form.get('age')
		phone = request.form.get('phone')
		email = request.form.get('email')
		if passwd == cpasswd:
			utils.signin(username,passwd,sex,age,phone,email,role)
		else:
			error = '2次密码不一致，please input again'
			return render_template('register.html',error=error)
	return renden_template('register.html',error=error)






















