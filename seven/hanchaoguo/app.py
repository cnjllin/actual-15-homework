#!/usr/bin/python
#coding:utf-8

from flask import Flask,render_template,request,redirect,session
from utils import insert,getone,select,update,delete
import json
app=Flask(__name__)
app.secret_key = 'askdmsakldalsdk'
filed = ['id','username','password','role']


#首页
@app.route('/',methods=['GET','POST'])
def sigin():
    if not session:
        return redirect('/login')
    username = "hanchaoguo"
    return render_template('index.html',username=username)


# 用户列表
@app.route('/userlist/')
def userlist():
    if not session:
        return redirect('/login/')
    res = select('user',filed)
    return  render_template('userlist.html',res=session,result=res['msg'])

# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        users = {k:v[0] for k,v in dict(request.form).items()}
        filed=['username','password','role']
        res =  insert('user',filed,users)
        if res['code'] == 0:
            return render_template ("reg.html",msg=res['msg'])
        else:
            return  render_template ("reg.html",mag=res['msg'])
    return render_template ("reg.html",msg=" ")


#登录
@app.route('/login/',methods=['GET','POST'])
def login():
   if request.method == 'POST':   
      dat = {k:v[0] for k,v in dict(request.form).items()}
      res = getone("user",filed,dat)
      if res['code'] == 0  and  res['msg']['password'] == dat['password']:
            session['username'] = dat['username']
            session['role'] = res['msg']['role']
            return json.dumps(res)
      else:
            return json.dumps(res)
   return  render_template('login.html',msg=" ") 

# 用户修改个人信息入口
@app.route('/userinfo1/')
def userinfo():
    if not session:
        return redirect('/login/')
    uid = request.args.get('id')
    data={'id':uid}
    res = getone("user",filed,data)
    data=res['msg']
    print data
    return json.dumps(data)
       

# 用户界面
@app.route('/userinfo/')
def usifo():
    if not session:
       return redirect('/login/')
    username = session['username']
    user_dict={'username':username}
    result=getone('user',filed,user_dict)
    return render_template('userinfo.html',res=session,result=result['msg'])


# 用户更新
@app.route('/update/',methods=['GET','POST'])
def up():
    if not session:
        return redirect('/logout/')
    dat = {k:v[0] for k,v in dict(request.form).items()}
    data = update("user",filed,dat)
    return json.dumps(data)

# 删除
@app.route('/delete/',methods = ['GET','POST'])
def delne():
    if not session:
        return redirect('/login/')
    data={k:v[0] for k,v in dict(request.args).items()}
    res = delete("user",filed,data)
    return json.dumps(res)

# 注销
@app.route('/logout/')
def logout():
    if session:
        session.clear()
    return redirect('/login/')
    

if __name__=='__main__':
    app.run(host='0.0.0.0',port=500,debug=True)
