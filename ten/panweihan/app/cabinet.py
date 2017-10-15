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

info_filename = "E:/Reboot15/homework/nine/tmp/info.log"
error_filename = "E:/Reboot15/homework/nine/tmp/error.log"

field = ['id','username','password','phone','role']
idc_field = ['id', 'name', 'name_cn', 'address', 'adminer', 'phone']
cabinet_field = ['id', 'name', 'idc_id', 'u_num', 'power', 'phone']

# 机柜列表
@app.route("/cabinet/")
def cabinet():
    if not session or session["role"] == 1:
        return redirect("/login/")
    result = db.getlist('cabinet', cabinet_field)
    result = result["msg"]
    for i in result:
        idc_data = {'id': i['idc_id']}
        idc_result = db.getone('idc',idc_field,idc_data)
        idc_result = idc_result['msg']
        i['idc_id'] = idc_result['name_cn']
    return render_template("cabinet.html",result = result)

# 添加机柜，并获取机房ID
@app.route("/cabinetadd/",methods=["GET","POST"])
def cabinetadd():
    if not session or session["role"] == 1:
        return redirect("/login/")
    if request.method == "GET":
        result = db.getlist('idc', idc_field)
        idc_id = result["msg"]
        return json.dumps(idc_id)
    if request.method == "POST":
        cabinet_field = ['id', 'name', 'idc_id', 'u_num', 'power']
        data = {k:v[0] for k, v in dict(request.form).items()}
        print data
        result = db.getone('cabinet', cabinet_field, data)
        if result['code'] == 0:
            return json.dumps("机柜名已被使用")
        else:
            cabinet_field = ['name', 'idc_id', 'u_num', 'power']
            result = db.insert('cabinet', cabinet_field, data)
            return json.dumps(result)
    #return render_template("cabinetadd.html",idc_id = idc_id)

# 更新机柜数据

# 更新机柜信息页面
@app.route("/cabinetupdate/",methods=["GET","POST"])
def cabinetupdate():
    if not session:
        return redirect("/login/")
    if request.method == "GET":
        idc = db.getlist('idc', idc_field)
        idc= idc["msg"]
        data = {k:v[0] for k, v in dict(request.args).items()}
        result = db.getone('cabinet', cabinet_field, data)
        result = result["msg"]
        return render_template("cabinetupdate.html", result=result, idc= idc)
    elif request.method == "POST":
        data = {k:v[0] for k, v in dict(request.form).items()}
        print data
        result = db.updata('cabinet', data)
        return json.dumps(result)

# 删除机柜
@app.route("/delete_cabinet/")
def delete_cabinet():
    if not session:
        return redirect("/login/")
    data = {k:v[0] for k, v in dict(request.args).items()}
    result = db.delete('cabinet', data)
    return json.dumps(result)