#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
from utile import insert,getone,update,check
import json
import util
from app import app


filed=["id","username","passwd","phone","email","age","sex","role"]



#—————用户管理


#用户注册
@app.route('/reg/',methods=["GET","POST"])
def reg():
    if request.method=="POST":
        file=["username","passwd","phone","email","age","sex","role"]
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=insert("mylist",file,user)
        if result["code"]==0    :
            return  json.dumps(result)
        else:
            return  json.dumps(result)


#用户信息
@app.route("/userinfo/")
def userinfo():
    if not session:
        return  redirect("/login/")
    data={'username':session['username']}
    result=getone("mylist",filed,data)
    print result
    if result["code"]==0:
        result=result["msg"]
    #return  json.dumps(result)
    return render_template("user.html",result=result)


#个人信息编辑
@app.route('/userupdate/',methods=['GET','POST'])
def userupdate():
    if not session:
       return redirect('/login/')
    if request.method=='POST':
       data={k:v[0] for k,v in dict(request.form).items()}
       result=update("mylist",filed,data)
    return  json.dumps(result)

#修改密码
@app.route('/updata/pwd/',methods=['GET','POST'])
def updatapwd():
    if not session:
       return redirect('/login/')
    if request.method=='POST':
        data={k:v[0] for k,v in dict(request.form).items()}
        print data
        userdata={"id":data["id"],"passwd":data["npassword"]}
        #result=update("mylist",filed,userdata)
        result=check("mylist",filed,userdata)
        if result["code"]==0:
            data={"id":data["id"],"passwd":data["npassword"]}
            result=update("mylist",filed,data)
    return  json.dumps(result)