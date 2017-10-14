#!/usr/bin/python
#_*_ coding:utf-8 _*_

from flask import Flask,render_template,redirect,session,request
from . import app
import json,utils,hashlib
import util

field = ['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']

#服务器列表页面
@app.route('/service/')
def service():
    if not session:
        return redirect('/login/')
    res = utils.getall('server',field)
    return render_template('server.html',info=session,result=res['msg'])


# 添加服务器
@app.route('/serveradd/',methods=['POST','GET'])
def serveradd():
    cab = ['id','cr','sr_id','u_num','power']
    field = ['hostname','lan_ip','wan_ip','cabinet_id','op','phone']
    if not session:
        return redirect('/login/')
    if request.method=='POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        print data
        result = utils.regist('server',field,data)
        return json.dumps(result)
    res = utils.getall('cabinet',cab)
    return render_template('serveradd.html',info=session,res=res['msg'])


# 编辑服务器信息
@app.route('/updateserver/',methods=['POST','GET'])
def updateserver():
    if not session:
        return redirect('/login/')
    if request.method == 'GET':
        data = {k:v[0] for k,v in dict(request.args).items()}
        res = utils.getone('server',field,data)
        return json.dumps(res['msg'])
    data = {k:v[0] for k,v in dict(request.form).items()}
    res = utils.update('server',field,data)
    return json.dumps(res)


# 删除服务器
@app.route('/serverdelete/',methods=['POST','GET'])
def serverdelete():
    if not session:
        return redirect('/login/')

    if request.method == 'POST':
        uid = request.form.get('id')
        result = utils.delete('server',uid)
        return json.dumps(result)
