#!/usr/bin/env python
#coding:utf-8

# 导入模块
from flask import Flask,request,render_template,redirect,session
import utils
import json

app = Flask(__name__)
app.secret_key="asdfgk"
field = ['id','username','password','tel','email','role']

# 首页
@app.route('/')
@app.route('/index/')
def index():    
    if not session:
                return redirect('/login/')
    if session['role'] == 0:
    	return redirect("/admin/")
    else:
	return redirect("/getone/")


#注册 
@app.route('/reg/',methods=['GET','POST'])
def register():
    if request.method=="POST":
        field = ['username','password','tel','email','role']
        data = {k:v[0] for k,v in dict(request.form).items()}
        result = utils.insert('user1',field,data)
        if result["code"] == 0:
	    return json.dumps(result) 
        else:
	    return json.dumps(result)
    return render_template('register.html')


# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
	data = {k:v[0] for k,v in dict(request.form).items()}
        result = utils.getone('user1',data,field)
        if result["code"] == 0:
            session['username'] = data['username']
            session['role'] = result['msg']['role']
	    return json.dumps(result)
	else:
	    res=utils.login('user1',data)
            if res['cod'] == 0:
	        res['errmsg'] = "password error"
	        return json.dumps(res)
            else:
                res['errmsg'] = "user is not exit"
                return json.dumps(res)
    return render_template('login.html')

#用户列表
@app.route('/userlist/')
def userlist():
	if not session or session['role'] != 0:
                return redirect('/login/')
	username = session['username']
        user = utils.userlist('user1')
        return render_template('userlist.html',username=username,user=user,info=session)


#管理员界面
@app.route('/admin/')
def admin():
	if not session:
                return redirect('/login/')
	username = session['username']
        result = utils.login('user1',username,field)
        if result['cod'] == 0:
                result = result['errmsg']
        return render_template("admin.html",username=username,result=result)

#普通用户界面
@app.route('/getone/')
def user():
	if not session:
                return redirect('/login/')
        username = session['username']
        result = utils.login('user1',username,field)
        if result['cod'] == 0:
                result = result['errmsg']
        return render_template("getone.html",username=username,result=result)




#添加用户
@app.route('/add/',methods=['GET','POST'])
def add():
	username = session['username']
	if request.method=="POST":
                field = ['username','password','tel','email','role']
                data = {k:v[0] for k,v in dict(request.form).items()}
                result = utils.insert('user1',field,data)
                if result["code"] == 0:
                        return redirect('/userlist/')
			#return json.dumps(result)
                else:
                        #return json.dumps(result)
			return render_template('add.html',username=username)
        return render_template('add.html',username=username)	


# 删除
@app.route('/delete/',methods=['GET','POST'])
def delete():
        if request.method=="GET":
                uid = request.args.get('id','')
                utils.delete('user1',uid)
                return redirect('/userlist/')
        return render_template('userlist.html')




#注销
@app.route('/logout/')
def logout():
        session.clear()
        return redirect('/login/')

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5001)
