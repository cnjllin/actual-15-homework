#!/usr/bin/python
#coding:utf-8

from flask import Flask,render_template,request,redirect,session
import json
app=Flask(__name__)
app.secret_key = 'adfagfagrehyrejutkyu'

field = ['id','username','password','role']

import utils

#首页
@app.route('/',methods=['GET','POST'])
def index():
#    if not session:
#        return redirect('/login/')
    username = "wd"
    return render_template('index.html',username=username)


#注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['username','password','role']
        insert_user = utils.insert('user',field,data)
        if insert_user['code'] == 0:
            return redirect('/login/')
        else:
            return render_template('reg.html',msg=insert_user)
    return render_template('reg.html',msg=" ")


#登录页面
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        dat = {k:v[0] for k,v in dict(request.form).items()}
        select_user = utils.getone('user',field,dat)
        
        if select_user['code'] == 0:
            if select_user['msg']['password']==dat['passwd']:
                session['username'] = dat['username']
                session['role'] = select_user['msg']['role']
                data = select_user
                return json.dumps(data)
            else:
                data = {'code':1,'msg':'passwd is wrong'}
                return json.dumps(data)
        else:
            data = {'code':1,'msg':'user not is exist'}
            return json.dumps(data)
        
    return render_template('login.html',msg=" ")


#用户列表
@app.route('/userlist/',methods=['GET','POST'])
def userlist():
    if not session:
        return redirect('/login/')
    else:
        user_all = utils.getall('user',field)
        return render_template('userlist.html',result=user_all['msg'],info=session)

#用户信息
@app.route('/userinfo/',methods=['GET','POST'])
def userinfo():
    if not session:
        return redirect('/login/')
    username = session['username']
    user={'username':username}
    result = utils.getone('user',field,user)
    if result['code']==0:
        result = result['msg']
    return render_template('userinfo.html',result=result)

#用户查询
@app.route('/get/')
def get():
    uid = request.args.get('id')
    user = {'id':uid}
    result=utils.getone('user',field,user)
    if result['code']==0:
        data=result['msg']
        print data
    return json.dumps(data)

#用户修改
@app.route('/update/',methods=['GET','POST'])
def modity():
    if not session:
        return redirect('/login/')
  
    if request.method == 'POST':
        user = {k:v[0] for k,v in dict(request.form).items()}
        data = utils.update('user',field,user)
        if data['code']==0:
            return json.dumps(data)
        #else:
            #return render_template('update.html',result=result)

#删除用户
@app.route('/delete/',methods=['GET'])
def delete():
    if not session:
        return redirect('/login/')
    uid = request.args.get('id')
    data = utils.dele('user',field,uid)
    return json.dumps(data)
        
#增加用户
@app.route('/add/',methods=['GET','POST'])
def add():
    if not session:
        return redirect('/login/')
    if request.method=="POST":
        field = ['username','password','role']
        user = {k:v[0] for k,v in dict(request.form).items()}
        data = utils.insert('user',field,user)
        return json.dumps(data)
    return render_template('add.html')


#用户退出
@app.route('/logout/')
def logout():
     if session:
         session.clear()
     return redirect('/login/')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
