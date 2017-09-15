#!/usr/bin/python
#coding:utf-8

from flask import Flask,render_template,request,redirect,session
import json
import utils
app=Flask(__name__)
app.secret_key = 'adfagfagrehyrejutkyu'

field = ['id','username','name','password','phone','mail','role','status']

#首页
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


#用户注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method=='POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['username','name','password','phone','mail','role','status']
        result = utils.getone("user",field,data)
        if result['code']==1:
            data = utils.regist('user',field,data)
            return json.dumps(data)
        else:
            data = {"code":1,"msg":"user is exist"}
            return json.dumps(data)
    return render_template('reg.html',msg=" ")

#用户登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=="POST":
        data={k:v[0] for k,v in dict(request.form).items()}
        result = utils.getone("user",field,data)
        if result['code']==0:
            if result['msg']['status'] ==0:
                if result['msg']['password']==data['password']:
                    session['username']=data['username']
                    session['role']=result['msg']['role']
                    result = {'code':0,'msg':'login success'}
                else:
                    result = {'code':1,'msg':'passwd is wrong'}
            else:
                result = {'code':1,'msg':'user is lock'}
        else:
            result = {'code':1,'msg':'user not is exist'}
        return json.dumps(result)
    return render_template('login.html',msg=' ')

#用户信息
@app.route('/userinfo/',methods=['GET','POST'])
def userinfo():
    if not session:
        return redirect('/login/')
    username=session['username']
    data={'username':username}
    result=utils.getone("user",field,data)
    if result['code']==0:
        result = result['msg']
    return render_template('userinfo.html',result=result,info=session)

#用户列表
@app.route('/userlist/',methods=['GET','POST'])
def userlist():
    if not session:
        return redirect('/login/')
    else:
        result = utils.getall("user",field)
        return render_template('userlist.html',result=result['msg'],info=session)

#更新个人资料
@app.route('/update/',methods=['GET','POST'])
def modity():
    if not session:
        return redirect('/login/')
    if request.method == "GET":
        data = {k:v[0] for k,v in dict(request.args).items()}
        return json.dumps(data)
    #if request.method == "POST":
    else:
        data = {k:v[0] for k,v in dict(request.form).items()}
        result = utils.update("user",field,data)
        return json.dumps(result)
    #if request.method == "GET":
    #else:
    #    data = {k:v[0] for k,v in dict(request.args).items()}
    #    print data
    #    return json.dumps(data)

#更新个人密码
@app.route('/ups/',methods=['GET','POST'])
def ups():
    if not session:
        return redirect('/login/')
    if request.method == "POST":
        oldpwd = {'password':request.form.get('oldpasswd')}
        newpwd = {'password':request.form.get('newpasswd')}
        username = session['username']
        user={'username':username}
        result = utils.getone('user',field,user)
        if result['msg']['password']==oldpwd['password']:
            if oldpwd['password']!= newpwd['password']:
                data = {'id':result['msg']['id'],'password':newpwd['password']}
                pwd = utils.update('user',newpwd,data)
                res = {'code':0,'msg':'update pwd success'}
            else:
                res = {'code':1,'msg':'The old pwd and new pwd can not same'}
        else:
            res = {'code':1,'msg':'old pwd is wrong'}
    return json.dumps(res)
       

#删除用户
@app.route('/delete/',methods=['GET','POST'])
def dele():
    if not session:
        return redirect('/login/')
    uid = request.args.get('id')
    result = utils.delete("user",uid)
    return json.dumps(result)

#添加用户
@app.route('/add/',methods=['GET','POST'])
def add():
    if not session:
        return redirect('/login/')
    if request.method == "POST":
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['username','name','password','phone','mail','role','status']
        result = utils.getone("user",field,data)
        if result['code']==1:
            res = utils.regist('user',field,data)
            return json.dumps(res)
        else:
            res = {"code":1,"msg":"user is exist"}
            return json.dumps(res)    
    return render_template('add.html',msg=" ",info=session)

#用户退出
@app.route("/logout/")
def logout():
    if session:
        session.clear()
    return redirect('/login/')


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
