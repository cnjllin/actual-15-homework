#!/usr/bin/env python
#-*- coding:utf-8 -*-

#------------------------------------
#      FileName: login.py
#          Desc:
#        Author: ruizhong.li
#       Version:
#    CreateTime: 2017-08-14
#------------------------------------

from flask import Flask
from flask import render_template
from flask import request
from judge import judge_register_user
from judge import judge_login_user

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    hello = "Welcome To My Home!"
    return render_template("index.html",hello=hello)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_name = request.form.get('nick_name','None')
        user_phone = request.form.get('mobile_num','None')
        user_passwd = request.form.get('password','None')
        ret = judge_register_user(user_name,user_phone,user_passwd)
        if ret != "":
            return render_template("register.html",error=ret)
        else:
            with open('./user_file','a+') as f:
                f.write("{0} {1} {2}".format(user_name,user_phone,user_passwd))
                f.write('\n')
            return render_template("successful.html",ret="Registration success")
    else:
        return render_template("register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        user_name = request.form.get('nick_name','None')
        user_passwd = request.form.get('password','None')
        ret = judge_login_user(user_name,user_passwd)
        if ret == "Login successful":
            return render_template("successful.html",ret=ret)
        else:
            return render_template("login.html",ret=ret)
    else:
        return render_template("login.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)


