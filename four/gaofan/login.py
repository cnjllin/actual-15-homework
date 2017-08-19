#!/usr/bin/python
# coding:utf-8
import string
import random
from flask import Flask,render_template,request
from user_manager_system import *
app=Flask(__name__)
database = shelve.open(datafile)

# 登录界面显示
@app.route('/login/',methods=["GET","POST"])
def index():
    global iden_code
    iden_code="".join(random.sample(string.letters+'0123456789',4))
    return render_template("login.html",iden_code=iden_code)

# 点击登录按钮后
@app.route('/login/userinfo/')
def display():
    name = request.args.get("name")
    password = request.args.get("password")
    if iden_code != request.args.get("iden_code"):
        return render_template("skip.html",error="incorrect identifying code")
    else:
        if login(name,password) != "login successfully":
            error = login(name,password)
            return render_template("skip.html",error=error)
        else:
            return render_template("login_userinfo.html",users=user_info(name),
                                   user_item=['name','age','job','tel','email'])

# 注册界面
@app.route('/login/register/',methods=["GET","POST"])
def registering():
    return render_template("register.html")

#点击注册界面后
@app.route('/login/register/check/')
def check():
    name = request.args.get('name')
    password1 = request.args.get('password1')
    password2 = request.args.get('password2')
    age = request.args.get('age')
    job = request.args.get('job')
    tel = request.args.get('tel')
    email = request.args.get('email')
    if user_register(name, password1, password2) == 'registered successfully':
        save_userinfo(name, password1, age, job, tel, email)
        return render_template('after_reg.html')
    else:
        error = user_register(name, password1, password2)
        return render_template('register.html',error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)
