#!/usr/bin/python 
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, request, render_template, redirect, session
from . import app
app.secret_key = "asdsdsdsdads"

import json

import db

import utils

import time

info_filename = "E:/Reboot15/homework/nine/tmp/info.log"
error_filename = "E:/Reboot15/homework/nine/tmp/error.log"

field = ['id','username','password','phone','role']
idc_field = ['id', 'name', 'name_cn', 'address', 'adminer', 'phone']
cabinet_field = ['id', 'name', 'idc_id', 'u_num', 'power', 'phone']
# 工单系统

jobs_field = ['id','apply_date','apply_type','apply_desc','deal_person','status','deal_desc','deal_time','apply_person']

# 添加工单
@app.route("/addjob/",methods=["GET","POST"])
def addjob():
    if not session.get('username',None):
        return redirect("/login/")
    if request.method == "POST":
        jobs_field = ['apply_date','apply_type','apply_desc','status','apply_person']
        data = {k:v[0] for k, v in dict(request.form).items()}
        data['apply_date'] = time.strftime("%Y-%m-%d %H:%M")
        data["status"] = 0
        data['apply_person'] = session['username']
        result = db.insert('ops_jobs', jobs_field, data)
        return json.dumps(result)
    return render_template("addjob.html")

# 工单列表
@app.route("/joblist/",methods=["GET","POST"])
def joblist():
    if not session.get('username',None):
        return redirect("/login/")
    result = db.getlist("ops_jobs",jobs_field)
    result = result['msg']
    for i in result:
        if i["status"] == 2:
            result.remove(i)
    return render_template("jobslist.html",result = result)

# 工单历史
@app.route("/jobhistory/",methods=["GET","POST"])
def jobhistory():
    if not session.get('username',None):
        return redirect("/login/")
    result = db.getlist("ops_jobs",jobs_field)
    result = result['msg']
    for i in result:
        if i["status"] == 0 and 1:
            result.remove(i)
    return render_template("jobhistory.html",result = result)

# 处理工单
@app.route("/jobupdate/",methods=["GET","POST"])
def jobbupdate():
    if not session.get('username',None):
        return redirect("/login/")
    if request.method == "POST":
        data = {k:v[0] for k, v in dict(request.form).items()}
        data['status'] = 2
        data['deal_person'] = session['username']
        data['deal_time'] = time.strftime("%Y-%m-%d %H:%M")
        result = db.updata("ops_jobs",data)
        return json.dumps(result)
    else:
        id = request.args.get('id')
        data = {'id': id,'status':1,"deal_person":session["username"],'deal_time':time.strftime("%Y-%m-%d %H:%M")}
        result = db.updata("ops_jobs",data)
        return json.dumps(result)

# 工单详情
@app.route("/jobdetail/",methods=["GET","POST"])
def jobdetail():
    if not session.get('username',None):
        return redirect("/login/")
    data = {k:v[0] for k, v in dict(request.args).items()}
    result = db.getone("ops_jobs",jobs_field,data)
    print result
    if not result:
        result = {"code":1,"msg":"信息查询失败"}
    return json.dumps(result)



