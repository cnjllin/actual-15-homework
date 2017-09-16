#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from utils import insert,getone,listall,updateuser,delete
import json

app = Flask(__name__)
app.secret_key="dsddddddffdsggdsgagdg"

field = ['id','username','password','role']

# 首页
@app.route('/')
@app.route('/index/')
def index():
    if not session:
        return redirect('/login/')
    return redirect("/userinfo/")

# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        user = { k:v[0] for k,v in dict(request.form).items()}
        result = insert('user1',field,user)
        if result['code'] == 0:
            return redirect('/login/')
        else:
            return render_template('reg.html',result=resutl)
    return render_template('reg.html')

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = { k:v[0] for k,v in dict(request.form).items()}
        result = getone('user1',field,data)
        if result['code'] == 0:
            if result['msg']['password'] == data['password']:
                session['username'] = data['username']
                session['role'] = result['msg']['role']
                return json.dumps(result)
            else:
                result['code'] = 1
                result['msg'] = '密码错误!'
                return json.dumps(result)
        else:
            result['msg'] = "用户名不存在!"
            return json.dumps(result)
    return render_template('login.html')

# 用户列表
@app.route('/userlist/')
def userlist():
    if session:
        if session['role'] == 0:
            result = listall('user1',field) 
            if result['code'] == 0:
                result = result['msg']
            return render_template('userlist.html',ret=result,session=session)
        else:
            return redirect('/userinfo/')
    return redirect('/login/')

# 个人信息
@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect('/login')
    data = {'username':session['username']}
    result = getone('user1',field,data)
    if result['code'] == 0:
        result = result['msg']
    return render_template("userinfo.html",user=result)

# 更新
@app.route('/update/',methods=['GET','POST'])
def update():
    if request.method == 'GET':
        userid = request.args.get('id')
        data={'id':userid}
        result = getone('user1',field,data)
        return json.dumps(result['msg'])
    else:
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        result = updateuser('user1',field,data)
        return json.dumps(result)
    return render_template('update.html')   

# 添加用户
@app.route("/add/",methods=['GET','POST'])
def add():
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        field = ['username','password','role']
        result = insert('user1',field,data)
        if result['code']==0:
            result['msg'] = "添加用户成功"
            return json.dumps(result)
        else:
            result['msg'] = "添加用户失败"
            return json.dumps(result)
    else:
        return render_template("add.html")

# 删除用户信息
@app.route('/delete/')
def delete_user():
    uid = int(request.args.get('id'))
    result = delete('user1',uid)
    return json.dumps(result)

# 销毁session
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
