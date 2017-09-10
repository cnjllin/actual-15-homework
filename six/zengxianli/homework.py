#! /bin/env python
#coding:utf-8
from flask import Flask,render_template,request,redirect

from utils import getone,insert,delete,updateid,list
import sys
reload(sys)
sys.setdefaultencoding('utf8')


field=['id','username','password','role']


app=Flask(__name__)





##打开首页
@app.route("/")
@app.route("/index/")
def index():
    username="zxl" 
    return render_template("index.html",username=username)

##打开注册页面
@app.route("/reg/",methods=["GET","POST"])
def reg():
    user={} 
    result={}
    if request.method=="POST":
        user=dict ((k,v[0]) for k,v in dict(request.form).items())
        result=getone('user',field,user)
        if result['code']==0:
            return render_template("reg1.html",result='该用户已被注册，请重新输入')
        elif not user['username']:
            return render_template("reg1.html",result="用户名为空，无法注册")
  	else: 
            insert('user',user)
            return  redirect('/login/')
    if request.method=="GET":
        return render_template("reg1.html")



##打开登陆页面
@app.route("/login/",methods=["GET","POST"])
def login():
    user={}
    result={}
    if request.method=="POST":
        user=dict ((k,v[0]) for k,v in dict(request.form).items())
        result=getone('user',field,user)
        if result['code']==1:
            return render_template("login.html",result=result['msg'])
        elif not user['username']:
            return render_template("login.html",result='用户名为空，无法登陆')
        else:
            result=getone('user',field,user)
            if result['code']==0 and result['msg']['password']==user['password']:
                return  redirect('/userlist/') 
            else:
                return render_template("login.html",result='密码错误，请重新输入')
    if request.method=="GET":
        return render_template("login.html")



##打开更新页面
@app.route("/update/",methods=["GET","POST"])
def update():
    if request.method=="POST":
        user=dict ((k,v[0]) for k,v in dict(request.form).items())
        updateid('user',user)
        return  redirect('/userlist/') 
    if request.method=="GET":
        uid=request.args.get('id',"")
        data={'id':uid}
        result=getone('user',field,data)
        return render_template("update.html",result=result['msg'])   



##展示用户列表页面
@app.route("/userlist/")
def userlist():
    uid=request.args.get('id')
    if uid:
        delete('user',uid)
    user=list('user',field)
    return render_template("userlist.html",result=user)


            
      

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)	        
