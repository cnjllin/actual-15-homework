#!/usr/bin/python
#coding:utf-8
from flask import Flask,render_template,request,redirect,session
from db import insert,getone,update,select,delete
import json
from db import insert,getone,update,select,delete
from . import app
filed2=['id','name','idc_id','u_num','power']
# 机柜信息列表
@app.route('/cabinet/',methods=['POST','GET'])
def cabinet():
    if not session:
        return redirect('/login/')
    res = select('cabinet',filed2)
    return render_template('cabinet.html',users=session,result=res['msg'])

# 添加机柜
@app.route('/cabinetadd/',methods=['POST','GET'])
def cabinetadd():
    filed2=['name','idc_id','u_num','power']
    filed1=['id','name','name_cn','address','adminer','phone']
    if not session:
        return redirect('/login/')
    if request.method=='POST':
        info={k:v[0] for k,v in dict(request.form).items()}
        result = insert('cabinet',filed2,info)
        if result['code']==0:
             return json.dumps(result)
        return json.dumps(result)
    res = select('idc',filed1)
    print res
    return render_template('cabinetadd.html',users=session,res=res['msg'])

# 删除机柜
@app.route('/cabinetdelete/',methods=['POST','GET'])
def cabinetdelete():
    if not session:
        return redirect('/login/')
    info = {k:v[0] for k,v in dict(request.form).items()}
    result=delete('cabinet',filed2,info)
    return json.dumps(result)



# 编辑机柜信息
@app.route('/updatecabinet/',methods=['POST','GET'])
def updatecabinet():
    if not session:
        return redirect('/login/')
    if request.method == 'GET':
        info={k:v[0] for k,v in dict(request.args).items()}
        res=getone('cabinet',filed2,info)
        if res['code']==0:
            return json.dumps(res['msg'])
        return json.dumps(res)
    info={k:v[0] for k,v in dict(request.form).items()}
    res=update('cabinet',filed2,info)
    if res['code']==0:
        return json.dumps(res)
    return json.dumps(res)


