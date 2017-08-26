#!/usr/bin/env python
#-*- coding:utf-8 -*-

#------------------------------------
#      FileName: app.py
#          Desc:
#        Author: ruizhong.li
#       Version:
#    CreateTime: 2017-08-24
#------------------------------------

from flask import Flask,render_template,request,redirect
from utils import *

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
        name = request.form.get('nick_name')
        sex = request.form.get('nick_sex')
        age = request.form.get('nick_age')
        phone = request.form.get('nick_phone')
        email = request.form.get('nick_email')
        passwd = request.form.get('nick_passwd')
        ret = judge_register_user(user_name,user_phone,user_passwd)
        if ret != "":
            return redirect("/register/",error=ret)
        else:
            insert(name,passwd,sex,age,phone,email)
            return redirect("/login/")
    return render_template("register.html")

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == "POST":
        user_name = request.form.get('nick_name')
        user_passwd = request.form.get('password')
        ret = judge_login_user(user_name,user_passwd)
        if ret == 0 and user_name == 'admin':
            return redirect("/userlist/")
        elif ret == 0 and user_name != 'admin':
            ret = select_name(user_name)
            return render_template("userinfo.html",ret=ret)
        else:
            return redirect("/login/",ret=ret)
    return render_template("login.html")


# 显示用户列表页面
@app.route('/userlist/')
def userlist():
    ret = select_all()
    return render_template("userlist.html",ret=ret)

# 更新用户信息
@app.route('/update/',methods=['GET','POST'])
def update_msg():
    if request.method == "GET":
        uid = int(request.args.get('id'))
        user_msg = select(uid)
        return render_template("update.html",user_msg=user_msg)
    elif request.method == "POST":
        user_id = int(request.form.get('user_id'))
        user_name = request.form.get('nick_name')
        phone_num = request.form.get('phone_num')
        npassword = request.form.get('npassword')
        update(user_name,phone_num,npassword,user_id)
        return redirect('/userlist/')
    else:
        return render_template("update.html")

# 删除用户信息
@app.route('/delete/')
def delete_user():
    uid = int(request.args.get('id'))
    delete(uid)
    return redirect('/userlist/')

# 增加用户信息
@app.route('/adduser/',methods=['GET','POST'])
def add_user():
    if request.method == "POST":
        name = request.form.get('nick_name')
        sex = request.form.get('nick_sex')
        age = request.form.get('nick_age')
        phone = request.form.get('nick_phone')
        email = request.form.get('nick_email')
        passwd = request.form.get('nick_passwd')
        insert(name,passwd,sex,age,phone,email)
        return redirect('/userlist/')
    else:
        return render_template("adduser.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)


