#!/usr/bin/env python
#coding:utf-8

from flask import Flask,render_template,request
import invoke

app = Flask(__name__)            ###相当于把Flask框架赋值给app，下面直接调用app变量即可

@app.route('/')
@app.route('/index')
def index_1():
	return render_template('index.html')




@app.route('/register',methods=['POST','GET'])
def reg():
	return render_template('signin.html')
	mtd = request.form if request.method == 'POST' else request.args
	name = mtd.get('username')
	password = mtd.get('passwd')
	print name,password
	register(name,password)


@app.route('/denglu',methods=['POST','GET'])
def login():
	return render_template('login.html')
        mtd = request.form if request.method == 'POST' else request.args
        name = mtd.get('username')
        password = mtd.get('passwd')
	print name,password
        login(name,password)

if __name__== '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
