#!/usr/bin/python 
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "asdsdsdsdads"

import json

import utils

field = ['id','username','password','role']

# 登录页面
@app.route("/",methods=["GET","POST"])
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = utils.getone('user', field, data)
        if result["code"] == 0:
            result = result["msg"]
            if result["password"] == data["password"]:
                session["username"] = data["username"]
                session["role"] = result["role"]
                return redirect("/userinfo/")
            else:
                return render_template("login.html",errmsg = "密码错误")
        else:
            return render_template("login.html",errmsg = "用户名错误")
    return render_template("login.html")


# 注册页面
@app.route("/reg/",methods=["GET","POST"])
def reg():
    if request.method == "POST":
        field = ['id','username','password','role']
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = utils.getone('user', field, data)
        if result['code'] == 0:
            return render_template("reg.html", errmsg="用户名已被使用")
        else:
            field = ['username','password','role']
            result = utils.insert('user',field,data)
            return redirect("/login/")
    return render_template("reg.html")

# 管理员页面
@app.route("/userlist/")
def userlist():
    if not session or session["role"] == 1:
        return redirect("/login/")
    result = utils.getlist('user',field)
    return render_template("userlist.html",result = result)


# 普通用户页面
@app.route("/userinfo/",methods=["GET","POST"])
def userinfo():
    if not session:
        return redirect("/login/")
    data = {"username":session["username"]}
    result = utils.getone('user', field, data)
    result = result["msg"]
    #return json.dumps(result)
    return render_template("userinfo.html", result=result)

# 获取用户信息接口
@app.route("/userjson/",methods=["GET","POST"])
def userjson():
    if not session:
        return redirect("/login/")
    data = {"username":session["username"]}
    result = utils.getone('user', field, data)
    result = result["msg"]
    return json.dumps(result)



# 更新页面
@app.route("/updata/",methods=["GET,POST"])
def updata():
    if not session:
        return redirect("/login/")
    uid = request.args.get("id", "")
    data = {"id": uid}
    result = utils.getone("user",field,data)
    if request.method == "POST":
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = utils.updata('user', data)
        return redirect()
    return render_template("updata.html", result)

# 退出登录
@app.route("/logout/")
def logout():
    session.clear()
    return redirect("/login/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
