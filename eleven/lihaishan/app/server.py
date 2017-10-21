#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
from utile import insert,getone,update,delete,list
import json
import util
from app import app

fileds_server = ['id','hostname', 'ip', 'mac', 'username', 'password', 'port', 'idc', 'brand', 'cpu', 'memory', 'disk', 'system_type', 'number',"cabinet"]
filed_idc=["id","username"]
cabinet_fields=['id','username']
#------------资产管理---服务器管理
@app.route("/severlist/")
def severlist():
    if not session:
        return  redirect("/login/")
    #result=list("server",fileds_server)["msg"]
    idcs=list("machine",filed_idc)
    cabinets   = list('cbten',cabinet_fields)
    servers  = list('server',fileds_server)
    #idcs={"%s" %idc["id"]:idc["username"] for idc in idcs}
    for cab  in servers['msg']:
        for items in cabinets['msg']:
            if  cab['cabinet'] == items['id']:
                cab['cabinet'] = items['username']
            for cac in idcs['msg']:
                if cab['idc'] == cac['id']:
                    cab['idc'] = cac['username']
    return render_template('severlist.html',result=servers['msg'])

    #return  render_template("severlist.html",result=result,idc=idcs)


#添加服务器
@app.route('/addsever/',methods=["GET","POST"])
def addsever():
    if 'username' not in  session:
        return redirect('/login/')
    if request.method=='GET':
        idc   =  list('machine',filed_idc)
        cabinet   =  list('cbten',cabinet_fields)
        result = {'code':0,'idc':idc['msg'],'cabinet':cabinet['msg']}
        return  json.dumps(result)
    if request.method=="POST":
        fileds = ['hostname', 'ip', 'mac', 'username', 'password', 'port', 'idc', 'brand', 'cpu', 'memory', 'disk', 'system_type', 'number',"cabinet"]
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=insert("server",fileds,user)
        print result
        if result["code"]==0    :
            return  json.dumps(result)


#编辑
@app.route('/updatesever/',methods=["GET","POST"])
def updatesever():
    if 'username' not in session:
        return  redirect("/login/")
    if request.method=="GET":
        id=request.args.get("id")
        data={"id":id}
        server = getone("server",fileds_server,data)
        idc  = list('machine',filed_idc)
        cabinet  = list('cbten',cabinet_fields)
        result = {'code':0,'idc':idc['msg'],'cabinet':cabinet['msg'],'server':server['msg']}
        return  json.dumps(result)
    else:
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=update("server",fileds_server,user)
        if result["code"]==0:
            return json.dumps(result)




#删除
@app.route('/dltsever/',methods=["GET","POST"])
def dlttsever():
    if 'username' not in  session:
        return redirect('/login/')
    data={k:v[0] for k,v in dict(request.form).items()}
    result=delete("server",data)
    return json.dumps(result)
