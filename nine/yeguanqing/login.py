#!/usr/bin/env python
#coding:utf-8
from flask import request,render_template, redirect,session
from utils import check
import json
import hashlib


@app.route('/')
@app.route('/login/',methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        data= {k:v[0] for k,v in dict(request.form).items()}
        field = ['username','password','role','status']
        where = {'username':data['username']}
        result = check('user',field,where)
        if  result['code'] == 0:
            if  int(result['msg']['status']) != 1:
                session['username'] = data['username']
                session['role']  = result['msg']['role'] 
                return json.dumps(result)
            else:
                result ={'code':1, 'msg':u"The user is locked."}
                return json.dumps(result)
        else:
            result ={'code':1, 'msg':u"The username or password is wrong."}
            return json.dumps(result)
    return render_template('login.html') 



@app.route('/logout/',methods=['GET', 'POST'])
def loginout():
    if session.get('username'):
        session.pop('username',None)
        session.pop('role',None)
    return redirect('/login/')

        

