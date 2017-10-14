#!/usr/bin/python
#coding:utf-8
from . import app
from flask import Flask,render_template,request,redirect,session
import json
from db import insert,getone,update,select,delete
from . import app
filed = ['id','username','name','password','phone','mail','role','status']

# 首页
@app.route('/')
def index():
    return render_template('index.html')


# 注册
@app.route('/reg/',methods=['POST','GET'])
def reg():
    filed = ['id','username','name','password','phone','mail','role']
    if request.method == 'POST':
        users = {k:v[0] for k,v in dict(request.form).items()}
        result = insert('user',filed,users)
        if result['code']==0:
            return render_template('login.html',msg=result['msg'])
        return render_template('reg.html',msg=result['errmsg'])
    return render_template('reg.html',msg="")



# 登录
@app.route('/login/',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        info = {k:v[0] for k,v in dict(request.form).items()}
        result = getone('user',filed,info)
        if  result['code'] == 0:
             if result['msg']['password'] == info['password']:
                   session['username'] = info['username']
                   session['role'] = result['msg']['role']
                   session['id'] = result['msg']['id']
                   return json.dumps(result)
             else:
                 result = {'errmsg':'passwd is error'}
                 return json.dumps(result)
        else:
             return json.dumps(result)
    return render_template('login.html')


# 用户个人主页
@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect('/login/')
    info = {k:v[0] for k,v in dict(request.args).items()}
    if info:
        users = getone('user',filed,info)
    else:
        users = getone('user',filed,session)
        print users
    return render_template('userinfo.html',users=users['msg'])

#查询单个用户信息
@app.route('/selectone/')
def selectone():
    if not session:
        return redirect('/login/')
    data={k:v[0] for k,v in dict(request.args).items()}
    result=getone('user',filed,data)
    if result['code']==0:
        res=result['msg']
        return json.dumps(res)
    return json.dumps(result)

# 更新用户信息
@app.route('/update/',methods=['POST','GET'])
def update1():
      filed=['id','username','name','phone','mail']
      if not session:
          return redirect('/login/')
      if request.method == 'POST':
          data={k:v[0] for k,v in dict(request.form).items()}
          result = update('user',filed,data)
          return json.dumps(result)
      return json.dumps(result)


# 修改个人密码
@app.route('/user/chpwdoneself',methods = ['POST','GET'])
def updatepassword():
     if not session:
         return redirect('/login/')
     info = {k:v[0] for k,v in dict(request.form).items()}
     users=getone('user',filed,session)
     if info['oldpasswd'] == users['msg']['password']:
          file = ['id','password']
          data={}
          data['password']=info['newpasswd']
          data['id']=session['id']
          result=update('user',file,data)
          return json.dumps(result)
     else:
         result = {'errmsg':'password is error'}
         return json.dumps(result)

# 用户列表
@app.route('/userlist/')
def userlist():
    if not session:
        return redirect('/login/')
    result=select('user',filed)
    if result['code']==0:
        return render_template('userlist.html',users=session,res=result['msg'])
    return render_template('userlist.html',users=session,res=result['errmsg'])

# 删除用户
@app.route('/delete/',methods=['POST','GET'])
def deleteUser():
    if not session:
        return redirect('/login/')
    info={k:v[0] for k,v in dict(request.args).items()}
    result=delete('user',filed,info)
    return json.dumps(result)


# 添加用户
@app.route('/adduser/',methods=['POST','GET'])
def adduser():
    filed = ['username','name','password','phone','mail','role','status']
    if not session:
        return redirect('/login/')
    if request.method=='POST':
        data={k:v[0] for k,v in dict(request.form).items()}
        result=insert('user',filed,data)
        return json.dumps(result)
    return render_template('adduser.html',users=session)



# 注销
@app.route('/logout/')
def logout():
    if session:
        session.clear()
    return redirect('/login/')



