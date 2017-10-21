#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
from utile import insert,getone,update,delete,list
import json
import util
from app import app

filed=["id","username","passwd","phone","email","age","sex","role"]


#用户界面
@app.route("/userlist/")
def  userlist():
    #if not session or session["role"]!=0:
    if not session:
        return redirect("/login/")
    result=list("mylist",filed)
    if result["code"]==0:
        result = result["msg"]
        return  render_template("new-userlist.html",result=result)


#用户更新
@app.route("/listupdate/",methods=["GET","POST"])
def listupdate():
    if not session:
        return  redirect("/login/")
    if request.method=="GET":
        uid=request.args.get("id","")
        data={"id":uid}
        result=getone("mylist",filed,data)
        if result["code"]==0:
            result=result["msg"]
        return  json.dumps(result)

#用户注册
@app.route('/reg/',methods=["GET","POST"])
def regist():
    if request.method=="POST":
        file=["username","passwd","phone","email","age","sex","role"]
        user=  {k:v[0]for k,v in dict(request.form).items()}#request.form 获取表格的值为[(username,lhs),(phone,18511891703)],通过字典进行遍历，获取key，values格式的数据
        result=insert("mylist",file,user)
        if result["code"]==0    :
            return  json.dumps(result)
        else:
            return  json.dumps(result)

#删除
@app.route("/dlt/")
def dlt():
    if not session:
        return  redirect("/login/")
    data={k:v[0] for k,v in dict(request.args).items()}
    result=delete("mylist",data)
    return json.dumps(result)
