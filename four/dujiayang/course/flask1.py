#!/usr/bin/env python
#coding:utf-8

from flask import Flask,render_template,request

app = Flask(__name__)        #相当于把Flask框架赋值给app，下面直接调用app变量即可

@app.route('/index')              #装饰器
@app.route('/')              #装饰器
def index():
	usersdict = {'name':'listhe','age':20}
	userslist = [{'name':'wd','age':18},{'name':'kk','age':20},{'name':'pc','age':19}]
	return render_template('index.html',thename='he',theage='1',list=userslist,dict=usersdict)

@app.route('/reg<string:name>/<string:passwd>')    ##http://127.0.0.1:5000/reg{'he':'ha'}/{'age':123} 不是字典，依然是字符串。
def reg(name,passwd):
	with open('user.txt','a+') as f:
		f.write("%s:%s\n"%(name,passwd))	
    	return "input %s%s ok" % (name,passwd)       ##input {'he':'ha'}{'age':123} ok   ---输出结果。

##http://127.0.0.1:5000/login?name=hehe&passwd=123
@app.route('/login')
def indexx():
	name = request.args.get('name')
	passwd = request.args.get('passwd')
	return "hello %s,u passwd is %s" %(name,passwd)

if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)
