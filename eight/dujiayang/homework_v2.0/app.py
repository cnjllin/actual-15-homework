#!/usr/bin/env  python
#coding:utf8

from flask import Flask,render_template,request,redirect,session
from utils import insert,getone,getlist,update 
import json
app = Flask(__name__)
app.secret_key="dsadfasfadsfasf"


field = ['id','username','password','role']

# 首页
@app.route("/")
@app.route("/index/")
def index():
    if not session:
        return redirect("/login")
    data = {'username':session['username']}
    result = getone('user',field,data)
    print result
    return render_template("index.html",info=result['msg'])

# 用户注册
@app.route("/reg/",methods=['GET','POST'])
def reg():
    if request.method == "POST":
            user = { k:v[0] for k,v in dict(request.form).items()}
            field = ['username','password','role']
            result = insert('user',field,user)
            if result['code'] == 0:
                return redirect('/login/')
            else:
                return render_template("reg.html",result = result)
    return render_template("reg.html")

# 用户登录
@app.route("/login/",methods=['GET','POST'])
def login():
    if request.method == "POST":
            data = { k:v[0] for k,v in dict(request.form).items()}
            result = getone('user',field,data)
	    print result
            if result['code'] == 0:
                 if result['msg']['password']==data['password']:
                     session['username'] = data['username']
                     session['role']=result['msg']['role']
                     print session 
                     if session['role']==0: 
                        return redirect('/userlist/')
                     else:
                        return redirect('/userinfo/')
                 else:
                    result['errmsg'] = "user is  exist, password is wrong"
                    
            else:
                result['errmsg'] = "user is not exist"
                return render_template("login.html",result = result)
    return render_template("login.html")


# 用户退出
@app.route("/logout/")
def logout():
    if session:
        session.clear()
    return redirect("/login")

# 用户列表
@app.route("/userlist/")
def userlist():
    if not session :
        return redirect("/login")
    result = getlist('user',field) 
    if result['code'] == 0:
        result = result['msg']
    return render_template("userlist.html",result=result,info = session)

# 用户信息
@app.route("/userinfo/")
def userinfo():
    if not session:
        return redirect("/login")
    uid = request.args.get('id',"")
    data = {'id':uid}
    result = getone('user',field,data) 
    if result['code'] == 0:
        result = result['msg']
    #return json.dumps(result)
    return render_template("update.html",result=result)

# 用户更新
@app.route('/update/',methods=['GET','POST'])
def modity():
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
     else:
        return render_template('update.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5566,debug=True)
