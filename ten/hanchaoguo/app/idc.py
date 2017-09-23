#!/usr/bin/python
#coding:utf-8
from flask import Flask,render_template,request,redirect,session
from db import insert,getone,update,select,delete
import json
from . import app
filed1=['id','name','name_cn','address','adminer','phone']

# 机房信息列表
@app.route('/idc/',methods=['POST','GET'])
def idc():
    if not session:
        return redirect('/login/')
    info={k:v[0] for k,v in dict(request.form).items()}
    res = select('idc',filed1)
    return render_template('idc.html',users=session,result=res['msg'])


# 编辑机房信息
@app.route('/updateidc/',methods=['POST','GET'])
def updateidc():
    if not session:
        return redirect('/login/')
    if request.method == 'GET':
        info={k:v[0] for k,v in dict(request.args).items()}
        res=getone('idc',filed1,info)
        if res['code']==0:
            return json.dumps(res['msg'])
        return json.dumps(res)
    info={k:v[0] for k,v in dict(request.form).items()}
    res=update('idc',filed1,info)
    return json.dumps(res)


# 删除机房
@app.route('/idcdelete/',methods=['POST','GET'])
def idcdelete():
    if not session:
        return redirect('/login/')
    info = {k:v[0] for k,v in dict(request.form).items()}
    result=delete('idc',filed1,info)
    return json.dumps(result)



# 添加机房
@app.route('/idcadd/',methods=['POST','GET'])
def idcadd():
    filed1=['name','name_cn','address','adminer','phone']
    if not session:
        return redirect('/login/')
    if request.method=='POST':
        info={k:v[0] for k,v in dict(request.form).items()}
        result = insert('idc',filed1,info)
        return json.dumps(result)
    return render_template('idcadd.html',users=session)






