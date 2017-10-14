#!/usr/bin/python
#coding:utf-8
from flask import Flask,render_template,request,redirect,session
#from utils import insert,getone,select,update,delete
from db import insert,getone,update,select,delete
import json
from db import insert,getone,update,select,delete
from . import app
filed3=['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']
# 添加服务器
@app.route('/serveradd/',methods=['POST','GET'])
def serveradd():
    filed2=['id','name','idc_id','u_num','power']
    filed3=['hostname','lan_ip','wan_ip','cabinet_id','op','phone']
    if not session:
        return redirect('/login/')
    if request.method=='POST':
        info={k:v[0] for k,v in dict(request.form).items()}
        result = insert('server',filed3,info)
        if result['code']==0:
             return json.dumps(result)
        return json.dumps(result)
    res = select('cabinet',filed2)
    return render_template('serveradd.html',users=session,res=res['msg'])

# 服务器信息列表
@app.route('/server/',methods=['POST','GET'])
def server():
    if not session:
        return redirect('/login/')
    res = select('server',filed3)
    return render_template('server.html',users=session,result=res['msg'])


# 编辑服务器信息
@app.route('/updateserver/',methods=['POST','GET'])
def updateserver():
    if not session:
        return redirect('/login/')
    if request.method == 'GET':
        info={k:v[0] for k,v in dict(request.args).items()}
        res=getone('server',filed3,info)
        if res['code']==0:
            return json.dumps(res['msg'])
        return json.dumps(res)
    info={k:v[0] for k,v in dict(request.form).items()}
    res=update('server',filed3,info)
    if res['code']==0:
        return json.dumps(res)
    return json.dumps(res)


# 删除服务器
@app.route('/serverdelete/',methods=['POST','GET'])
def serverdelete():
    if not session:
        return redirect('/login/')
    info = {k:v[0] for k,v in dict(request.form).items()}
    result=delete('server',filed3,info)
    return json.dumps(result)


