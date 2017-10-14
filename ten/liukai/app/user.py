#! /usr/bin/env python
# __*__coding:utf-8__*__
from flask import Flask,request,render_template,redirect,session
import utils
import json
import util
from .import app 

table="user"
field=['id','username','name','password','phone','email','role','status']

# 首页
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}   
       field=['username','name','password','phone','email','role','status']
       res=utils.get_one(table,field,user_dict)
       if res['code']==0:
           result=utils.insert(table,field,user_dict)
           util.WriteLog("register","/tmp/info.log").info("register:%s"%user_dict["username"])
           return json.dumps(result)
       else:
           result={'code':1,'msg':'register username is already exists'}
           util.WriteLog("register","/tmp/error.log").info("register:%s"%result['msg'])
           return json.dumps(result)
    return render_template('reg.html')
           

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        user=utils.get_one(table,field,user_dict)
        if user['code']==0 and user_dict['password']==user['msg']['password']:
            if user['msg']['status']==0:
               session['username']=user_dict['username']
               session['role']=user['msg']['role']
               util.WriteLog("login","/tmp/info.log").info('login:%s'%session['username'])
               return json.dumps(user)
            else:
               data={'code':1,'msg':'username is locking'}
               util.WriteLog("login_error","/tmp/error.log").error('login_error:%s'%data['msg'])
               return json.dump(data)
        else:
            data={'code':1,'msg':'username or password is error'}
            util.WriteLog("login_error","/tmp/error.log").error('login_error:%s'%data['msg'])
            return json.dumps(data)  
    return render_template("login.html")

# 用户个人页
@app.route('/user/')
def user():
    if not session:
        return redirect("/")
    username=session['username']
    user_dict={'username':username}
    util.WriteLog("getone","/tmp/info.log").info('get_one:%s'%session['username'])
    result=utils.get_one(table,field,user_dict)
    return render_template('list.html',res=session,result=result['msg'])

# 用户列表
@app.route('/userlist/')
def userlist():
    if not session:
        return redirect('/')
    util.WriteLog("list","/tmp/info.log").info("list:%s"%session['username'])
    result=utils.list(table,field)    
    if result['code']==0:
        return render_template('userlist.html',res=session,result=result['msg'])
 
# 增加用户
@app.route('/add/',methods=['POST'])
def add():
    if not session:
        return redirect("/")
    if request.method=="POST":
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        field=['username','name','password','phone','email','role','status']
        result=utils.insert(table,field,user_dict)
        if result['code']==0:
            util.WriteLog("insert","/tmp/info.log").info("inster:%s"%session['username'])
            data=result
            return json.dumps(data)
        else:
            util.WriteLog("insert_error","/tmp/error.log").info("inster_error:%s"%session['username'])
            data={'code':1,'msg':'insert is error'}
            return json.dumps(data)

# 删除用户
@app.route('/delete/')
def delete():
    if not session:
        return redirect('/')
    uid=request.args.get('id')
    util.WriteLog("delete","/tmp/info.log").info("delete:%s"%session['username'])
    data=utils.delete(table,uid)
    return json.dumps(data)


# 编辑用户
@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect('/')
    uid=request.args.get('id')
    data={'id':uid}
    result=utils.get_one(table,field,data)
    util.WriteLog("userinfo","/tmp/info.log").info("userinfo:%s"%session['username'])
    if result['code']==0:
        data=result['msg']
        return json.dumps(data)
    
# 更新
@app.route('/update/',methods=['GET','POST'])
def update():
    if not session:
       return redirect('/')
    if request.method=="POST":
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       print user_dict
       if user_dict.has_key('oldpasswd'):
           username=session['username']
           data1={'username',username}
           result=utils.get_one(table,field,data1)
           if user_dict['oldpasswd']==result['msg']['password']:
               info={}
               field=['id','password']
               info['id']=result['msg']['id']
               info['password']=user_dict['newpasswd']
               util.WriteLog("update_psswd","/tmp/info.log").info("update_passwd:%s"%session['username'])
               data=utils.update(table,field,info)
               return json.dumps(data)
           else:
               result={'code':1,'msg':'oldpasswd is error'}
               util.WriteLog('update_passwd','/tmp/error.log').error("update_password:%s"%session['username'])  
               return json.dumps(result)    
       else:
           field=[]
           util.WriteLog("update","/tmp/info.log").info("update:%s"%session['username'])
           data=utils.update(table,field,user_dict)
           return json.dumps(data)







































