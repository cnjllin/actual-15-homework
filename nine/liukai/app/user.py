#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
import utils
import json
import  util
from . import app

table="user"
field=['id','username','name','password','phone','email','role','status']
#############用户权限管理########################

# 首页
@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        field=['username','name','password','phone','email','role','status']
        user=utils.get_one(table,field,user_dict)
        if user['code']==1:
            result=utils.insert(table,field,user_dict)
            util.WriteLog("res").info("res:%s"%user_dict['username'])
            return json.dumps(result)
        else:
            result={'code':1,'msg':'username is error '}
            return json.dumps(result)
    return render_template("reg.html")
      
# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        user=utils.get_one(table,field,user_dict)
        if  user['code']==0  and  user_dict['password']==user['msg']['password']:
           if user['msg']['status']==0:
               session['username']=user_dict['username']
               session['role']=user['msg']['role']
               data=user
               util.WriteLog("login").info("login:%s"%session['username'])
               return json.dumps(data)
           else:
               data={'code':1,'msg':'username is locking'}
               return json.dumps(data)
        else:
           data={'code':1,'msg':'username or password  is error'}
           return json.dumps(data)
    return render_template("login.html")

# 用户界面
@app.route('/user/')
def user():
    if not session:
        return redirect('/')
    username=session['username']
    user_dict={'username':username}
    util.WriteLog("get_one").info("get_one:%s"%session['username'])
    result=utils.get_one(table,field,user_dict)
    return render_template('list.html',res=session ,result=result['msg'])


# 管理员用户列表
@app.route('/userlist/')
def userlist():
    if session:
        util.WriteLog("list").info("list:%s"%session['username'])
        result=utils.list(table,field)
        if result['code']==0:
            return render_template('userlist.html',res=session,result=result['msg'])
        else:
            result={'code':1,'msg':'username or password  is error'}
            return render_template("login.html",result=result)
    else:
        return redirect("/login/")

# 管理员添加用户
@app.route('/add/',methods=['GET','POST'])
def add():
    if not session:
        return redirect('/')
    if request.method=='POST':
        user={k:v[0] for k,v in dict(request.form).items()}
        field=['username','name','password','email','role','status']
        if user['username'] and user['password']:
            util.WriteLog("insert").info("insert:%s"%session['username'])
            data=utils.insert(table,field,user)
            return json.dumps(data)
        else:
           data={'code':1,'errmsg':'username or password is not null'}
           return json.dumps(data)
    return render_template("add.html",res=session)


# 删除   
@app.route('/delete/',methods=['GET','POST'])
def delete():
    if not session:
       return redirect('/')
    uid=request.args.get('id')
    util.WriteLog("delete").info("delete:%s"%session['username'])
    data=utils.delete(table,uid)
    return json.dumps(data)

# 修改界面
@app.route('/userinfo/',methods=['GET','POST'])
def userinfo():
     if not session:
         return redirect('/')
     if request.method=='GET':
         uid=request.args.get('id')
         data={'id':uid}
         result=utils.get_one(table,field,data)
         util.WriteLog("userinfo").info("userinfo:%s"%session['username'])
         if result['code']==0:
            result=result['msg']
     return json.dumps(result)

# 刷新
@app.route('/update/',methods=['GET','POST'])
def update():
    if not session:
       return redirect('/')
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       util.WriteLog("update").info("update:%s"%session['username'])
       data=utils.update(table,field,user_dict)
       return  json.dumps(data)

# 用户登出
@app.route("/logout/")
def logout():
   if session:
      util.WriteLog("logout").info("logout:%s"%session['username'])
      session.clear()
   return redirect("/")


