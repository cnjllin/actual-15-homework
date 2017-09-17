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

field = ['id','username','password','phone','role']

# 登录页面
@app.route("/login",methods=["GET","POST"])
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = utils.getone('user', field, data)
        if result["code"] == 0:
            if result['msg']["password"] == data["password"]:
                session["username"] = data["username"]
                session["role"] = result['msg']["role"]
                data = result
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


# 用户信息页面
@app.route("/")
def userinfo():
    if not session:
        return redirect("/login/")
    data = {"username":session["username"]}
    result = utils.getone('user', field, data)
    result = result["msg"]
    # return json.dumps(result)
    return render_template("userinfo.html", result=result)

# 用户信息接口
@app.route("/getuser/")
def getuser():
    if not session:
        return redirect("/login/")
    data = {k:v[0] for k, v in dict(request.args).items()}
    result = utils.getone('user', field, data)
    result = result["msg"]
    return json.dumps(result)

# 更新页面
@app.route("/updata/",methods=["GET","POST"])
def updata():
    if not session:
        return redirect("/login/")
    if request.method == "POST":
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = utils.updata('user', data)
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
        result = utils.getone('user', field, user)
        result = result['msg']
        if data['oldpasswd'] == result['password']:
            user["password"] = data["newpasswd"]
            result = utils.updata('user', user)
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
    result = utils.delete('user', data)
    print result
    return json.dumps(result)

# 退出登录
@app.route("/logout/")
def logout():
    session.clear()
    return redirect("/login/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
