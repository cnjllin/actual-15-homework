#!/usr/bin/env python
#coding:utf8

from flask import Flask,request,redirect,render_template

app= Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
	username = "wd"
	render_template("index.html",username=username)

@app.route('/reg/',methods=['POST','GET'])
def reg():
	if request.method == "POST":
		data = {k:v[0] for k,v in dict(request.form).iteritems()}	
		print data
		field = ["username","passwd","role"]
		result = insert('dudjiayang',field,data)
		if result['code'] == 0:
			return render_template("index.html",result=result)
			#return redirect('/login/')
		else:
			return render_template("register.html",result=result)
	return render_template("register.html")


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
