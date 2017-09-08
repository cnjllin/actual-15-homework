#!/usr/bin/env python
#coding:utf-8

from flask import Flask, render_template, request, redirect, session
from utils import insert, getone, list, update, del_user
import json

app = Flask(__name__)
app.secret_key='xerxes'
#field = ['id','username','password','role']
field = ['id','username','password']

# 首页
@app.route("/")
@app.route("/index/")
def index():
    if not session:
        return redirect('/login/')
    username = "xerxes"
    return render_template("index.html",username=username)

# 注册
@app.route("/reg/",methods=["GET","POST"])
def reg():
    if request.method == "POST":
        user = {k:v[0] for k,v in dict(request.form).items()}
        field = ['username','password']
        result = insert('user',field,user)
        if result['code'] == 0:
            return redirect('/login/')
        else:
            return render_template("reg.html",result=result)
    return render_template("reg.html")

# 登录
@app.route("/login/",methods=['GET','POST'])
def login():
    field = ['id','username','password']
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        print data
        #{'username': u'tt', 'commit': u'\u767b\u5f55', 'password': u'tt'}
        result = getone('user',field,data)
        if result['code'] == 0:
            print result['msg']
            #{'username': 24, 'password': u'tt'}
            if result['msg']['password']==data['password']:
                session['username']=data['username']
                return redirect('/')
            else:
                result['errmsg'] = "user is exist.passowrd is wrong"
        else:
            result['errmsg'] = 'user is not exist'
            return render_template("login.html",result=result)
    return render_template("login.html")

# 退出
@app.route("/logout/")
def logout():
    if session:
        session.clear()
    return redirect('/login/')

# 用户列表
@app.route("/userlist/",methods=['POST','GET'])
def userlist():
    if not session:
        return redirect('/login/')
    result = list('user',field)
    if result['code'] == 0:
        result = result['msg']
    return render_template("userlist.html",result=result)

# 用户信息
@app.route("/userinfo/")
def userinfo():
    if not session:
        return redirect("/login/")
    uid = request.args.get('id',"")
    data = {'id':uid}
    result = getone('user',field,data)
    if result['code'] == 0:
        result = result['msg']
    return json.dumps(result)
    # return render_template("update.html",result=result)

# 用户更新
@app.route("/update/",methods=['GET','POST'])
def modity():
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        result = update('user',field,data)
        if result['code']==0:
            return redirect('/userlist/')
        else:
            return render_template("update.html",result=result)
    else:
        uid = request.args.get("id","")
        data = {'id':uid}
        result = getone('user',field,data)
        if result['code'] == 0:
            result = result['msg']
        return render_template("update.html",result=result)

# 用户删除
@app.route("/del/",methods=['GET','POST'])
def deluser():
    if request.method == 'GET':
        userid = request.args.get('id')
        del_user(userid)
        return redirect('/userlist/')
    #return render_template("userlist.html",result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
