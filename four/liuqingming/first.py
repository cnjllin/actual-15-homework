#!/bin/env python
# -*- coding:utf-8 -*-

import ngnix   #生成IP_top10.html
from classUser import User   #导入User类
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/reg/',methods=['GET', 'POST'])
def reg():
    if request.method == 'POST' :
        username = request.form.get('user')
        passwd = request.form.get('pwd')
        passwd1 = request.form.get('pwd1')
        if passwd == passwd1 :
            new_user = User(username,passwd)
            if not new_user.user_get() :
                new_user.user_reg()
                return "register success, your name is %s" % (username)
            else:
                return "%s already exists" % username
        else :
            return "The two password is different"
        
    return render_template("reg.html")

@app.route('/login/',methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        name = request.form.get('user')
        passwd = request.form.get('pwd')
        user_tmp = User(name, passwd)
        if user_tmp.user_get() == False :
            zhuche = '<a href="/reg/">Register</a>'
            return "%s user name does not exist \n %s" % (name, zhuche) 
        elif user_tmp.user_get() == passwd :
            #return "Hello %s, login success ,Welcome back " % (name,passwd)
            return render_template("IP_top10.html")
        else :
            return "password is error! " 
    return render_template("login.html")

@app.route('/')
@app.route('/index/',methods=['GET', 'POST'])
def index():
    #str = "Hello world ! index"
    #users = [ {'name':'wd','age':18,'role':1},{'name':'kk','age':20,'role':2},{'name':'pc','age':19,'role':0} ]
    #return render_template("user.html",'123',str = str,users = users)
    return render_template("IP_top10.html")
    

if __name__ == '__main__' :
    app.run(host='0.0.0.0',port=5000,debug=True)
