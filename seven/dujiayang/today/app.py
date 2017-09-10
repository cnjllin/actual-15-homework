#!/usr/bin/env python
#coding:utf-8
from flask import Flask,render_template,request
import json

app = Flask(__name__)

@app.route('/')
def userlist():
    return render_template("userlist.html")

@app.route('/login/',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).iteritems()}
		result = {'code':0,'msg':data}
		#print result
		return json.dumps(result)
    	return render_template("login.html")


@app.route('/getone/')
def getone():
	username = request.args.get("username","")
	user = {'name':username,'passwd':'123456'}
	return json.dumps(user)

#@app.route('/')
#def hello_world():
#    name="liuziping"
#    return render_template("userlist.html",user_name=name)

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=9999)
