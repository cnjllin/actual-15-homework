#!/usr/bin/python
#_*_ coding:utf-8 _*_

from flask import Flask,render_template,redirect,session,request
from . import app
import json,utils,hashlib
import util

field = ['id','sr','srfn','address','manager','phone']

#显示机房列表
@app.route('/idc/',methods=['GET','POST'])
def idc():
    if not session:
        return redirect('/login/')
    res=utils.getall("idc",field)
    return render_template('idc.html',res=res['msg'],info=session)


#增加机房
@app.route('/addidc/',methods=['GET','POST'])
def addidc():
    if not session:
        return redirect('/login/')
    if request.method == 'POST':
        field = ['sr','srfn','address','manager','phone']
        data = {k:v[0] for k,v in dict(request.form).items()}
        res = utils.getone('idc',field,data)
        if res['code']==1:
            result = utils.regist('idc',field,data)
        else:
            result = {'code':1,'msg':'server root is exist!'}
        return json.dumps(result)


#显示机房信息
@app.route('/didc/',methods=['GET','POST'])
def disidc():
    data = {k:v[0] for k,v in dict(request.args).items()}
    res = utils.getone('idc',field,data)
    return json.dumps(res['msg'])

#编辑修改机房
@app.route('/updateidc/',methods=['GET','POST'])
def updateidc():
    if not session:
        return redirect('/login/')

    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        res = utils.getone('idc',field,data)
        if res['code']==1:
            res = utils.update('idc',field,data)
        else:
            res = {'code':1,'msg':'server room is exist'}
        return json.dumps(res)

#删除机房
@app.route('/idcdel/',methods=['GET','POST'])
def idcdel():
    if not session:
        return redirect('/login/')
    if request.method == 'POST':
        uid = request.form.get('id')
        result = utils.delete('idc',uid)
        return json.dumps(result)

