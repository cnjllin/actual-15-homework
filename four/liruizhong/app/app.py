#!/usr/bin/env python
#-*- coding:utf-8 -*-

#------------------------------------
#      FileName: login.py
#          Desc:
#        Author: ruizhong.li
#       Version:
#    CreateTime: 2017-08-14
#------------------------------------

from flask import Flask,render_template,request,redirect
from util import judge_register_user,judge_login_user

app = Flask(__name__)

# 首页
@app.route('/')
@app.route('/index/')
def index():
    hello = "Welcome To My Home!"
    return render_template("index.html",hello=hello)

# 注册
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_name = request.form.get('nick_name','None')
        user_phone = request.form.get('mobile_num','None')
        user_passwd = request.form.get('password','None')
        ret = judge_register_user(user_name,user_phone,user_passwd)
        if ret != "":
            return redirect("/register/",error=ret)
        else:
            with open('./user_file','a+') as f:
                f.write("{0} {1} {2}".format(user_name,user_phone,user_passwd))
                f.write('\n')
            return redirect("/login/")
    return render_template("register.html")

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == "POST":
        user_name = request.form.get('nick_name','None')
        user_passwd = request.form.get('password','None')
        ret = judge_login_user(user_name,user_passwd)
        if ret == "Login successful":
            return redirect("/index/")
        else:
            return redirect("/login/",ret=ret)
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)


