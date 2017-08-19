#!/usr/bin/python
# -*- coding:utf-8 -*-
# **********************************************************
# * Author        : louxiaohui
# * Email         : 1031138448@qq.com
# * Last modified : 2017-08-14 00:58
# * Filename      : sample_flask.py
# * Description   : 
# * ********************************************************
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/reg/<string:user>/<string:passwd>/')
def reg(user,passwd):
    print user,passwd
    with open ("user_info","a+") as f:
        f.write('%s %s\n' %(user,passwd))
    return 'congratulation,%s,register successfully.' % user

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/after-login/',methods=['GET','POST'])
def afterlogin():
    return render_template("login.html",error='username or password is error')
    if request.method=="POST":
        username = request.form.get('username')
        passwd = request.form.get('passwd')
    else:
        username = request.args.get('username')
        passwd = request.args.get('passwd')
    if username=='lxh' and passwd=='123456':
        return 'hello %s,your password is %s' % (username,passwd)
    else:
        return render_template("login.html",error='username or password is error')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
