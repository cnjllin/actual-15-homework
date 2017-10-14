#!/usr/bin/python
#_*_ coding:utf-8 _*_

from flask import Flask,render_template,redirect,session,request
from . import app
import json,utils,hashlib
import util


field = ['id','cr','sr_id','u_num','power']
idc_field = ['id','sr','srfn','address','manager','phone']
#机柜列表页面
@app.route('/cabinet/')
def cabinet():
    if not session:
        return redirect ('/login/')
    cab = utils.getall('cabinet',field)['msg']
    idcs = utils.getall('idc',idc_field)['msg']
    idc = {'%s' %idc['id']:idc['sr'] for idc in idcs}
    for n in cab:
        if n['sr_id'] in idc:
            n['sr_id'] = idc[n['sr_id']]
            
    return render_template('cabinet.html',result=cab,info=session)

#增加机柜
@app.route('/addcn/',methods=['GET','POST'])
def addcn():
    field = ['cr','sr_id','u_num','power']
    if not session:
        return redirect ('/login/')
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        print data
        result = utils.regist('cabinet',field,data)
        return json.dumps(result)
    res = utils.getall('idc',idc_field)
    print res['msg']
    return render_template('addcn.html',info=session,res=res['msg'])


###编辑机柜
@app.route('/cabinetupdate/',methods=['POST','GET'])
def updatecabinet():
    if not session:
        return redirect('/login/')
    if request.method == 'GET':
        data={k:v[0] for k,v in dict(request.args).items()}
        res=utils.getone('cabinet',field,data)
        return json.dumps(res['msg'])
    data={k:v[0] for k,v in dict(request.form).items()}
    print data
    res=utils.update('cabinet',field,data)
    print "test --> %s" %res
    return json.dumps(res)


#删除机柜
@app.route('/deletecn/',methods=['POST'])
def deletecn():
    if not session:
        return redirect ('/login/')
    if request.method == 'POST':
        uid = request.form.get('id')
        result = utils.delete('cabinet',uid)
        print result
        return json.dumps(result)
