#!/usr/bin/env python
#coding:utf-8
#-----------------------------------
#     FileName: CMDB.py
#         Desc:
#       Author: copy
#      Version:
#     CreatTime: 2017-09-02
# ----------------------------------

from flask import Flask,render_template,request,redirect,session
from utils import insert,getone,getlist,update
import json

app = Flask(__name__)
app.secret_key="cfcfdedjededubhfgrflkh"
field = ['id','username','password','role']

# 首页
@app.route("/")
@app.route("/index/")
def index():
    if not session:
        return redirect("/login")
    username = "yaoxin"
    return render_template("index.html",username=username)

@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        user = {k:v[0] for k,v in dict(request.form).items()}
        print user
        field = ['username','password','role']
        result = insert('user',field,user)
        if result['code'] == 0:
            return redirect('/login/')
        else:
            return render_template("reg.html",result=result)
    return render_template("reg.html")


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()} 
        result = getone('user',field,data)
        if result['code'] == 0:
            if result['msg']['password'] == data['password']:
                session['username'] = data['username']
                session['role'] = result['msg']['role']
                print session
                if session['role']==0:
                    return redirect('/userlist/')
                else:
                    return redirect('/')
            else: 
                result['errmsg'] = "user is exite password is wrong"
        else:
             result['errmsg'] = "user is not exite"
             return render_template("login.html",result=result)              
    return render_template('login.html')


@app.route('/userlist/')
def userlist():
    if not session:
        return redirect("/login")
    result = getlist('user',field)
    if result['code'] == 0:
        result = result['msg']
    return render_template("userlist.html",result=result,info=session)

@app.route('/update/',methods=['GET','POST'])
def modify():
    if not session:
        return redirect("/login")
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        result = update('user',field,data)
        if result['code']==0:
            return redirect("/userlist/")
        else:
            return render_template('update.html',result=result)
    return render_template('update.html')


@app.route("/userinfo/")
def userinfo():
    if not session:
        return redirect("/login")
    uid=request.args.get('id',"")
    data = {'id':uid}
    result = getone('user',field,data)
    if result['code'] == 0:
        result = result['msg']
    # return json.dumps(result)
    return render_template('update.html',result=result)

@app.route('/delete/')
def delete():
	if not session:
		return redirect('/login')
	uid = request.args.get('id')
	user_dict = {'id':uid}
	result = delete('user',user_dict)
	if result['code'] == 0:
		return redirect('/userlist/')

@app.route("/logout/")
def logout():
    if session:
        session.clear()
    return redirect("/login")

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1234,debug=True)