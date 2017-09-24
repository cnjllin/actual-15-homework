#!/usr/bin/env python
#coding:utf-8

from flask import request,render_template, redirect,session
from utils import  getone,check,_update,_delete,insert_sql
from sessions import sessioninfo
import json

@app.route('/center/')
def  center():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessioninfo()
    field  = ["id","username","name_cn","password","mobile","email","role","status"]
    data={'username':session['username']}
    result  = getone('user',data,field)
    return render_template('center.html',msg=result['msg'])

@app.route('/user/chpwdoneself',methods=['GET', 'POST'])
def chpwdoneself():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessioninfo()
    chpwd = {k:v[0] for k,v in dict(request.form).items()}
    where = {'id':chpwd['id'],'password':chpwd['oldpasswd']}
    field = ['id','password']
    result = check('user',field,where)
    if  result['code'] == 0:
        data =  {'id':chpwd['id'],'password':chpwd['newpasswd']}
        result = _update('user',field,data)
    else:
        result ={'code':1, 'msg':u"The password is rong, please input again."}
    return json.dumps(result)

@app.route('/user/chmessageoneself',methods=['GET', 'POST'])
def chmessageoneself():
    if 'username' not in  session:
        return redirect('/login/')
    msg = sessioninfo()
    if request.method=='POST':
        field  = ["username","name_cn","mobile","email"]
        user = {k:v[0] for k,v in dict(request.form).items()}
        result = _update('user',field,user)
        if  result['code'] == 0:
            result ={'code':0, 'msg':"add user success"}
            return json.dumps(result)
