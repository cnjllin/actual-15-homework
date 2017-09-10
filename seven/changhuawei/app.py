#!/usr/bin/env python
#coding:utf-8

from flask import Flask,request,render_template,redirect,session
from util import insert,getone,getlist,update
import sys,json
reload(sys)
sys.setdefaultencoding('utf8')
app = Flask(__name__)
filed = ['id','username','password','role','email']
app.secret_key="dsadfasfadsfasf"

# 首页
@app.route('/')
@app.route('/index/')
def index():
    if not session:
        return redirect('/login')
    print session
    username = 'changhuawei'
    return render_template("index.html",username=username)
# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method == 'POST': 
        user = {k:v[0] for k,v in dict(request.form).items()}
        print user 
        filed = ['username','password','role','email']
        result = insert('user',filed,user)
        if result['code'] == 0:
            return redirect('/login/')
        else:
            return render_template('reg.html',result=result)
    return render_template('reg.html')
# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = {k:v[0] for k,v in dict(request.form).items()}
        res = getone('user',filed,user)
        if res['code'] == 0:
            if res['msg']['password'] == user['password']:
                session['username'] = user['username']
                session['role'] = res['msg']['role']
                if session['role'] == 0:
                    return redirect('/userlist/')
                else:
                    return redirect('/')
            else:
                res['errmsg']='passwd err'
                return render_template('login.html',result=res)
        else:
            res['errmsg']='user is not exit'
            return render_template('login.html',result=res)
    return render_template('login.html')


@app.route('/userlist/')
def userlist():
    if not session or session['role'] != 0:
        return redirect('/login')
    res = getlist('user',filed)
    if session['role'] ==0:
        res = res['msg']
    return render_template('userlist.html',result=res)


@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect('/login')
    uid = request.args.get('id',"")
    data = {'id':uid}
    result = getone('user',filed,data)
    if result['code'] ==0:
        result = result['msg']
    # return json.dumps(result)
        return render_template('update.html',result=result)



@app.route('/logout/')
def logout():
    if session:
        session.clear()
    return redirect('/login/')



@app.route('/update/',methods=['GET','POST'])
def modity():
    if not session:
        return redirect('/login')
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        result = update('user',filed,data)
        if result['code']==0:
               return redirect("/userlist/")
        else:
                 return render_template('update.html',result=result)
    else:
        uid = request.args.get('id',"")
        data = {'id':uid}
        result = getone('user',filed,data)
        if result['code'] ==0:
            result = result['msg']
        return render_template('update.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True )

