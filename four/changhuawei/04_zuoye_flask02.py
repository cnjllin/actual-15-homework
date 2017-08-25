#!/usr/bin/env python
#coding:utf-8

from flask import Flask,request,render_template
import sys

app = Flask(__name__)
#注册
# @app.route('/reg/<string:name>/<string:passwd>')
@app.route('/login/', methods=['GET', 'POST'])
def reg():
	if request.method == 'POST':
		#获取用户输入
		username = request.form.get('name')
		passwd = request.form.get('passwd')
		# print username,passwd
	else:
		username = request.args.get('name')
		passwd = request.args.get('passwd')
	with open('yonghu.txt','a+') as f:
		f.write("%s:%s\n" % (username,passwd))
	# return '注册成功'
	return render_template("reg.html",username = username)

@app.route('/')
@app.route('/index')
def index():

	return render_template("zhuce.html")
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5001,debug=True ) 
