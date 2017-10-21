#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
from utile import insert,getone,update,delete,list
import json
import util
from app import app




filed_idc=["id","username","address","phone"]

#机房管理界面
@app.route("/machinlist/")
def machinlist():
    if not session:
        return  redirect("/login/")
    result=list("machine",filed_idc)
    if result["code"]==0:
        result = result["msg"]
    return  render_template("machine.html",result=result)


#添加机房
@app.route('/machinreg/',methods=["GET","POST"])
def machinreg():
    if request.method=="POST":
        file=["username","address","phone"]
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=insert("machine",file,user)
        print result
        if result["code"]==0    :
            return  json.dumps(result)
        else:
            return  json.dumps(result)


#机房更新
@app.route("/machinupdate/",methods=["GET","POST"])
def machinupdate():
    if not session:
        return  redirect("/login")
    filed=["username","address","phone"]
    if request.method=='POST':
        datas=request.form
        data={k:v[0] for k,v in dict(request.form).items()}
        print data
        print datas
        result=update("machine",filed,data)
        return  json.dumps(result)
    else:
        uid=request.args.get("id","")
        data={"id":uid}
        result=getone("machine",filed_idc,data)
        #return  json.dumps(result)
        return  render_template("machinupdate.html",idc=result["msg"])

#机房删除
@app.route("/machindlt/")
def machindlt():
    if not session:
        return  redirect("/login/")
    data={k:v[0] for k,v in dict(request.args).items()}
    result=delete("machine",data)
    return json.dumps(result)
