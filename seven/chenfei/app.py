#!/usr/bin/python 
# __*__ coding: UTF-8 __*__

from flask import Flask,render_template,request,redirect,session
from utils import insert,getone,list,update,delete
import json
app = Flask(__name__)
app.secret_key="dsadfasfadsfasf"

field = ['id','username','password','role']


# 首页
@app.route('/')
@app.route('/index/')
def index():
    username="ceo"
    return  render_template('index.html',username=username) 

# 用户注册:
@app.route('/add/',methods=['GET','POST'])
def reg():
    if request.method == "POST":
           user = { k:v[0] for k,v in dict(request.form).items()} 
           print user
           field = ['username','password','role']
           result = insert('user',field,user)
           print result
           if result['code'] == 0:
               return redirect("/login/")
           else: 
               return render_template("reg.html",result = result)
    return render_template("reg.html")          

# 用户登录
@app.route("/login/",methods=['GET','POST'])
def login():
    if request.method == "POST":
           data = { k:v[0] for k,v in dict(request.form).items()}
           result = getone('user',field,data)
           if result['code'] == 0 and result['msg']['password'] == data['password']:
              return redirect('/userlist')
           else:
              result['errmsg'] = "user is exist,password is wrong"
    return render_template("login.html")

# 用户列表
@app.route("/userlist/")
def userlist():
    result = list('user',field)
    if result['code'] == 0:
        result = result['msg']
    return render_template("userlist.html",result=result)

# 用户信息
@app.route("/userinfo/")
def userinfo():
    uid = request.args.get('id',"")
    data = {'id':uid}
    result = getone('user',field,data)
    if result['code'] == 0:
        result = result['msg']
    result=json.dumps(result)
    return render_template("userinfo.html",result=result)

#用户更新
@app.route('/update/',methods=['GET','POST'])
def modity():
     if request.method == 'POST':
        data = dict(request.form)
        data = { k:v[0] for k,v in data.items()}
        result = update('user',field,data)
        if result['code']==0:
              return redirect("/userlist/")
        else:
             return render_template('update.html',resdult=result)
     else:
        uid = request.args.get('id',"")
        data = {'id':uid}
        result = getone('user',field,data)
        if result['code'] == 0:
             result = result['msg']
        return render_template('update.html',result=result)
# 用户删除
@app.route('/del/')
def deleteuser():
        uid=request.args.get('id')
        data={'id':uid}
        print data
        result = delete(data)
        return redirect('/userlist/')
# 用户注销
@app.route('/logout/')
def logout():
    session.clear()
    return render_template("index.html")


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8082,debug=True)
