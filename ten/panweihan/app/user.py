#!/usr/bin/python 
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, request, render_template, redirect, session
from . import app

app.secret_key = "asdsdsdsdads"

import json

import db

import utils

import time

info_filename = "E:/Reboot15/homework/nine/tmp/info.log"
error_filename = "E:/Reboot15/homework/nine/tmp/error.log"

field = ['id','username','password','phone','role']
idc_field = ['id', 'name', 'name_cn', 'address', 'adminer', 'phone']
cabinet_field = ['id', 'name', 'idc_id', 'u_num', 'power', 'phone']

# 登录页面
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = db.getone('user', field, data)
        if result["code"] == 0:
            if result['msg']["password"] == data["password"]:
                session["username"] = data["username"]
                session["role"] = result['msg']["role"]
                data = result
                utils.WriteLog("app模块", info_filename).info("%s用户登录系统" %session["username"])
                return json.dumps(data)
            else:
                data['errmsg'] = "密码错误"
                return json.dumps(data)
        else:
                data['errmsg'] = "用户名错误"
                return json.dumps(data)
    return render_template("login.html")


# 注册页面
@app.route("/reg/",methods=["GET","POST"])
def reg():
    if request.method == "POST":
        field = ['id','username','password','role']
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = db.getone('user', field, data)
        if result['code'] == 0:
            return render_template("reg.html", errmsg="用户名已被使用")
        else:
            field = ['username','password','role']
            result = db.insert('user', field, data)
            return redirect("/login/")
    return render_template("reg.html")

# 管理员查看所有用户页面
@app.route("/userlist/")
def userlist():
    if not session or session["role"] == 1:
        return redirect("/login/")
    result = db.getlist('user', field)
    result = result["msg"]
    print result
    return render_template("userlist.html",result = result)


# 用户信息页面
@app.route("/")
def userinfo():
    if not session:
        return redirect("/login/")
    data = {"username":session["username"]}
    result = db.getone('user', field, data)
    result = result["msg"]
    # return json.dumps(result)
    return render_template("userinfo.html", result=result)

# 用户信息接口
@app.route("/getuser/")

def getuser():
    if not session:
        return redirect("/login/")
    data = {k:v[0] for k, v in dict(request.args).items()}
    result = db.getone('user', field, data)
    result = result["msg"]
    print result
    return json.dumps(result)

# 更新用户信息页面
@app.route("/updata/",methods=["GET","POST"])
def updata():
    if not session:
        return redirect("/login/")
    if request.method == "POST":
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = db.updata('user', data)
        return json.dumps(result)
    #return render_template("updata.html")

# 用户修改密码
@app.route("/user/chpwdoneself/",methods=["GET","POST"])
def chpwdoneself():
    if not session:
        return redirect("/login/")
    if request.method == "POST":
        data = {k:v[0] for k, v in dict(request.form).items()}
        user = {}
        user["id"] = data["id"]
        result = db.getone('user', field, user)
        result = result['msg']
        if data['oldpasswd'] == result['password']:
            user["password"] = data["newpasswd"]
            result = db.updata('user', user)
            return json.dumps(result)
        else:
            result = {'errmsg':"原密码错误"}
            return json.dumps(result)

# 删除用户
@app.route("/delete/")
def delete():
    if not session:
        return redirect("/login/")
    data = {k:v[0] for k, v in dict(request.args).items()}
    result = db.delete('user', data)
    return json.dumps(result)

# 退出登录
@app.route("/logout/")
def logout():
    session.clear()
    return redirect("/login/")