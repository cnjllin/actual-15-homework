#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
from utile import insert,getone,update,delete,list
import json
import util
from app import app

filed=["id","username","passwd","phone","email","age","sex","role","status"]

#用户登录
@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        data={k:v[0]for k,v in dict(request.form).items()}
        result=getone("mylist",filed,data)
        if result["code"]==0:
            if result["msg"]["passwd"]==data["passwd"]:
                session["username"]=data["username"]
                session["role"]=result["msg"]["role"]
                util.WriteLog("user").info("%s login succesful" %session["username"])
                #print(json.dumps(result))
                return json.dumps(result)
        else:
            result["errmsg"]="passwd is wrong"
            return json.dumps(result)
    return render_template("login.html")

#用户退出
@app.route("/logout/")
def logout():
    if session:
        session.clear()
    return  redirect("/login/")