#!/usr/bin/env python
#-*- coding:utf-8 -*-

#------------------------------------
#      FileName: app.py
#          Desc:
#        Author: ruizhong.li
#       Version:
#    CreateTime: 2017-09-02
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
        msg = dict(request.form)
        info = dict((k,v[0]) for k,v in msg.items())
        ret = judge_register_user(**info)
        if ret != "":
            return redirect("/register/")
        else:
            fields,values = [],[]
            for k,v in info.items():
                fields.append(k)
                values.append("'%s'"% v)
            sql = "insert into user(%s) values(%s)" % (','.join(fields),','.join(values))
            insert(sql)
            return redirect("/login/")
    return render_template("register.html")

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == "POST":
        msg = dict(request.form)
        info = dict((k,v[0]) for k,v in msg.items())
        ret = judge_login_user(**info)
        if ret == 0:
            user_msg = select_name(info['name'])
            if user_msg['role'] == 0:
                return redirect("/userlist/")
            else:
                return render_template("userinfo.html",ret=user_msg)
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
        msg = dict(request.form)
        info = dict((k,v[0]) for k,v in msg.items())
        sql = "update user set username='%(username)s',phone='%(phone)s',password='%(password)s' where id = %(id)s" % info
        update(sql)
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
        msg = dict(request.form)
        info = dict((k,v[0]) for k,v in msg.items())
        fields,values = [],[]
        for k,v in info.items():
            fields.append(k)
            values.append("'%s'"% v)
        sql = "insert into user(%s) values(%s)" % (','.join(fields),','.join(values))
        insert(sql)
        return redirect('/userlist/')
    else:
        return render_template("adduser.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)


