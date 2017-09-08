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
        #uid = request.args.get('id')
        #dat = {'id':uid}
        select_user = utils.getone('user',field,dat)
        #data = select_user
        #return json.dumps(data)
        
        if select_user['code'] == 0:
            if select_user['msg']['password']==dat['passwd']:
                session['username'] = dat['username']
                session['role'] = select_user['msg']['role']
                data = select_user
                return json.dumps(data)
                #if session['role']==0:
                #return redirect('/userlist/')
                #else:
                #    return redirect('/login/')
            else:
                data = {'code':1,'msg':'passwd is wrong'}
                #return json.dumps(data)
                return render_template('login.html',msg=msg)
        else:
            data = {'code':1,'msg':'user not is exist'}
            return json.dumps(data)
            #return render_template('login.html',msg=msg)
        
    return render_template('login.html',msg=" ")


#用户列表
@app.route('/userlist/',methods=['GET','POST'])
def userlist():
    if not session:
        return redirect('/login/')
    else:
        user_all = utils.getall('user',field)
        return render_template('userlist.html',user=user_all['msg'],info=session)

#用户信息
@app.route('/userinfo/',methods=['GET','POST'])
def userinfo():
    if not session:
        return redirect('/login/')
    #uid = request.args.get('id')
    #data = {'id':uid}
    username = session['username']
    data={'username':username}
    result = utils.getone('user',field,data)
    if result['code']==0:
        result = result['msg']
    #return json.dumps(result)
    return render_template('userinfo.html',result=result)

#用户更新
@app.route('/update/',methods=['GET','POST'])
def modity():
    if not session:
        return redirect('/login/')
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        result = utils.update('user',field,data)
        if result['code']==0:
            return redirect("/userlist/")
        else:
            return render_template('update.html',result=result)


#用户退出
@app.route('/logout/')
def logout():
     if session:
         session.clear()
     return redirect('/login/')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
