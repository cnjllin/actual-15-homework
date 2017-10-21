#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
from utile import insert,getone,update,delete,list
import json
import util
from app import app

filed_cbt=["id","username","address","U","power"]
filed_idc=["id","username","address","phone"]

#机柜管理界面
@app.route("/cbtenlist/")
def cbtenlist():
    if not session:
        return  redirect("/login/")
    cab=list("cbten",filed_cbt)["msg"]
    idcs=list("machine",filed_idc)["msg"]
    idc={"%s" %idc["id"]:idc["username"] for idc in idcs}
    for i in cab:
         if i["address"] in idc:
             i["address"]=idc[i["address"]]
    return  render_template("cbtenlist.html",result=cab,idc=idcs)

#用户更新
@app.route("/cbtenupdate/",methods=["GET","POST"])
def cbtenupdate():
    if not session:
        return  redirect("/login/")
    if request.method=='POST':
        data={k:v[0] for k,v in dict(request.form).items()}
        result=update("cbten",filed_cbt,data)
        return  json.dumps(result)
    else:
        uid=request.args.get("id","")
        data={"id":uid}
        result=getone("cbten",filed_cbt,data)
        idc=list("machine",filed_idc)["msg"]
        if result["code"]==0:
            result=result["msg"]
        #return  json.dumps(result)
        return  render_template("cbtenupdate.html",result=result,idc=idc)

#添加机柜
@app.route('/cbtenreg/',methods=["GET","POST"])
def cbtenreg():
    if request.method=="POST":
        file=["username","address","U","power"]
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=insert("cbten",file,user)
        print result
        if result["code"]==0    :
            return  json.dumps(result)
        else:
            return  json.dumps(result)

#机柜删除
@app.route("/cbtendlt/")
def cbtendlt():
    if not session:
        return  redirect("/login/")
    data={k:v[0] for k,v in dict(request.args).items()}
    result=delete("cbten",data)
    return json.dumps(result)