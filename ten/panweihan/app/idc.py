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


# 获取机房所有信息
@app.route("/idc/")
def idc():
    if not session or session["role"] == 1:
        return redirect("/login/")
    result = db.getlist('idc', idc_field)
    result = result["msg"]
    return render_template("idc.html",result = result)

# 添加机房
@app.route("/addidc/",methods=["GET","POST"])
def addidc():
    if request.method == "POST":
        idc_field = ['id','name', 'name_cn', 'address', 'adminer', 'phone']
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = db.getone('idc', idc_field, data)
        if result['code'] == 0:
            return json.dumps("机房名已被使用")
        else:
            idc_field = ['name', 'name_cn', 'address', 'adminer', 'phone']
            result = db.insert('idc', idc_field, data)
            return json.dumps(result)
    return render_template("idc.html")

# 根据ID获取单个机房信息
@app.route("/getidc/")
def getidc():
    if not session:
        return redirect("/login/")
    data = {k:v[0] for k, v in dict(request.args).items()}
    result = db.getone('idc', idc_field, data)
    result = result["msg"]
    return json.dumps(result)

# 更新机房信息页面
@app.route("/updata_idc/",methods=["GET","POST"])
def updata_idc():
    if not session:
        return redirect("/login/")
    if request.method == "POST":
        data = {k:v[0] for k, v in dict(request.form).items()}
        result = db.updata('idc', data)
        return json.dumps(result)

# 删除机房
@app.route("/delete_idc/")
def delete_idc():
    if not session:
        return redirect("/login/")
    data = {k:v[0] for k, v in dict(request.args).items()}
    result = db.delete('idc', data)
    return json.dumps(result)
