#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
from app import app

# 机房列表
@app.route('/idc/')
def idc():
    if session:
        if session['role'] == 'admin':
            field = ['id','name','name_cn','address','adminer','phone']
            result = listall('idc',field) 
            if result['code'] == 0:
                result = result['msg']
            return render_template('idc/idc.html',ret=result,session=session)
        else:
            return redirect('/')
    return redirect('/login/')

# 添加机房
@app.route("/idcadd",methods=['GET','POST'])
def idcadd():
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        print data
        field = ['name','name_cn','address','adminer','phone']
        result = insert('idc',field,data)
        if result['code']==0:
            result['msg'] = "添加机房成功"
            return json.dumps(result)
        else:
            result['msg'] = "添加机房失败"
            return json.dumps(result)
    else:
        return render_template("/idc/idcadd.html")
