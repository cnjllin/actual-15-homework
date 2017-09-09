#!/usr/bin/env python
#coding:utf-8

from flask import Flask,render_template,request
import invoke

app = Flask(__name__)            ###相当于把Flask框架赋值给app，下面直接调用app变量即可

@app.route('/')
@app.route('/index')
def index_1():
	return render_template('index.html')


#@app.route('/zhuceye',methods=['POST','GET'])
#def sigin():
#	return render_template('zhuceye.html')
	
@app.route('/zhuce',methods=['POST','GET'])
def reg():
	if request.method == 'POST':
	name = request.form.get('username')
	password = request.form.get('passwd')
	invoke.register(name,password)
	return "congratulation,%s reged is ok" %name


@app.route('/denglu',methods=['POST','GET'])
def login():
	return render_template('login.html')
        mtd = request.form if request.method == 'POST' else request.args
        name = mtd.get('username')
        password = mtd.get('passwd')
        login(name,password)

if __name__== '__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
