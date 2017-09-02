#!/usr/bin/env python
#-*- coding:utf-8 -*-

#-----------------------------------
#     FileName: CMDB.py
#         Desc:
#       Author: copy
#      Version:
#     CreatTime: 2017-09-02
# ----------------------------------

from flask import Flask,render_template,request,redirect
import utils

app = Flask(__name__)

# 首页
@app.route("/")
@app.route("/index/")
def index():
    username = "yaoxin"
    return render_template("index.html",username=username)

@app.route("/register/", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = { k:v[0] for k,v in dict(request.form).items()}
        res = utils.register(data)
        if res['code'] == 0:
            return redirect('/login/')
        elif res['code'] == 1:
            return render_template('register.html',res=res)
    else:
        res={'msg':''}
        return render_template("register.html",res=res)

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data={k:v[0] for k,v in dict(request.form).items()}
        res = utils.login(data)
        if res['code'] == 0:
            if utils.role(data)[0] == 0:
                return redirect('/admin/')
            else:
                return render_template('userinfo.html',res=res)
        else:
            return render_template('login.html',res=res)
    else:
        res={'msg':''}
        return render_template('login.html',res=res)

@app.route('/admin/')
def admin():
    return render_template('admin.html')

@app.route('/userlist/')
def userlist():
    data=utils.userlist()
    return render_template('userlist.html',res=res)

@app.route('/deleteuser/')
def deleteuser():
    uid=request.args.get('id')
    data={'id':uid}
    utils.delete(data)
    return redirect('/userlist/')

@app.route('/update/',methods=['GET','POST'])
def update():
    if request.method=='POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        res =utils.update(data)
        if res['code']==0:
            return redirect('/userlist/')
        else:
            return render_templates('update.html',res=res)
    else:
        uid=request.args.get('id')
        data={'id':uid}
        res=utils.getuser(data)
        return render_template('update.html',res=res)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1234,debug=True)