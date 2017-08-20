#!/usr/bin/env python
#coding:utf-8

from flask import Flask,request,render_template
import sys

app = Flask(__name__)
#注册
@app.route('/reg/<string:name>/<string:passwd>')
def reg(name,passwd):
	with open('yonghu.txt','a+') as f:
		f.write("%s:%s\n" % (name,passwd))
	# return '注册成功'
	return render_template("reg.html",username = name)

#登录
@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		#获取用户输入
		username = request.form.get('name')
		passwd = request.form.get('passwd')
		# print username,passwd
	else:
		username = request.args.get('name')
		passwd = request.args.get('passwd')
	data = {}
	#获取用户，密码，定义到data字典
	with open('yonghu.txt') as f: 
		for line in f:
			users = line.rstrip().split(":")
			data[users[0]] = users[-1]
	#判断用户在不在data，并判断密码
	if username in data:
		if passwd == data[username]:
			#返回render 用户名到前端渲染
		    return render_template("login.html",username = username)
		else:
			return 'passwd err'
	else:
		return 'name err'
#首页
@app.route('/')
@app.route('/index')
def index():
	# name = 'chw'
	# age = '18'
	# user = {'name':'wd','age':'18','role':'0'}
	# score = ['10','9','8']
	# users = [{'name':'wd','age':'18'},{'name':'xx','age':'20'},{'name':'chw','age':'19'}]
	# return render_template("index.html",username = name,age = age)
	# return render_template("index1.html",score = score,user = user,users = users)
	return render_template("index.html")
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True )   
