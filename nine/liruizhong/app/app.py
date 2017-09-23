#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
import json

app = Flask(__name__)
app.secret_key="dsddddddffdsggdsgagdg"

field = ['id','name','name_cn','password','email','mobile','role','status','create_time','last_time']

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
        result = insert('users',field,user)
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
        field = ['name','password','role','status']
        result = getone('users',field,data)
        if result['code'] == 0:
            if result['msg']['password'] == data['password']:
                WriteLog("login").info("%s login success" % data['name'])
                session['name'] = data['name']
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
        if session['role'] == 'admin':
            result = listall('users',field) 
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
        return redirect('/login/')
    data = {'name':session['name']}
    result = getone('users',field,data)
    if result['code'] == 0:
        result = result['msg']
    return render_template("userinfo.html",user=result)

# 更新
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method == 'GET':
        userid = request.args.get('id')
        data={'id':userid}
        field = ['id','name','name_cn','email','mobile','role','status']
        result = getone('users',field,data)
        return json.dumps(result['msg'])
    else:
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        print data
        field = ['name','name_cn','email','mobile','role','status']
        result = updateuser('users',field,data)
        return json.dumps(result)
    return render_template('update.html')   

# 修改密码
@app.route('/chpwdoneself/',methods=['POST'])
def chpwdoneself():
    if not session:
        return redirect('/login/')
    passwd = dict(request.form)
    passwd = {k:v[0] for k,v in passwd.items()}
    data = {'name':session['name']}
    field = ['id','name','password']
    result = getone('users',field,data)
    if result['msg']['password'] == passwd['oldpasswd']:
        result['msg']['password'] = passwd['newpasswd']
        field = ['password']
        result = updateuser('users',field,data=result['msg'])
    else:
        result ={'code':1, 'msg':u"旧密码不正确请重新输入!"}
    return json.dumps(result)

# 添加用户
@app.route("/add/",methods=['GET','POST'])
def add():
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        field = ['username','password','role']
        result = insert('users',field,data)
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
    result = delete('users',uid)
    return json.dumps(result)

# 销毁session
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')

# 机房列表
@app.route('/idc/')
def idc():
    if session:
        if session['role'] == 'admin':
            field = ['id','name','name_cn','address','adminer','phone']
            result = listall('idc',field) 
            if result['code'] == 0:
                result = result['msg']
            return render_template('idc/idc.html',ret=result,session=session)
        else:
            return redirect('/')
    return redirect('/login/')

# 添加机房
@app.route("/idcadd",methods=['GET','POST'])
def idcadd():
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        print data
        field = ['name','name_cn','address','adminer','phone']
        result = insert('idc',field,data)
        if result['code']==0:
            result['msg'] = "添加机房成功"
            return json.dumps(result)
        else:
            result['msg'] = "添加机房失败"
            return json.dumps(result)
    else:
        return render_template("idc/idcadd.html")

# 删除机房信息
@app.route('/idcdelete')
def delete_idc():
    uid = int(request.args.get('id'))
    result = delete('idc',uid)
    return json.dumps(result)

# 机柜更新
@app.route('/idcupdate',methods=['GET','POST'])
def idcupdate():
    if request.method == 'GET':
        userid = request.args.get('id')
        data={'id':userid}
        field = ['id','name','name_cn','address','adminer','phone']
        result = getone('idc',field,data)
        ret = result['msg']
    else:
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        field = ['name','name_cn','address','adminer','phone']
        result = updateuser('idc',field,data)
        return json.dumps(result)
    return render_template('idc/idcupdate.html',idc=ret)   

# 机柜列表
@app.route('/cabinet/')
def cabinet():
    if session:
        if session['role'] == 'admin':
            field = ['id','name','idc_id','u_num','power']
            result = listall('cabinet',field) 
            if result['code'] == 0:
                result = result['msg']
            return render_template('cabinet/cabinet.html',ret=result,session=session)
        else:
            return redirect('/')
    return redirect('/login/')

# 服务器列表
@app.route('/server/')
def server():
    if session:
        if session['role'] == 'admin':
            field = ['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']
            result = listall('server',field) 
            if result['code'] == 0:
                result = result['msg']
            return render_template('server/server.html',ret=result,session=session)
        else:
            return redirect('/')
    return redirect('/login/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
