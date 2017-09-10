#!/usr/bin/python
#coding:utf-8
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
	username = "wd"
	return render_template('index.html',username=username)


# 注册
@app.route('/reg/',methods=['GET','POST'])
def register():	
	if request.method=="POST":
		field = ['username','password','tel','email','role']
		data = {k:v[0] for k,v in dict(request.form).items()}
		result = utils.insert('user1',field,data)
		if result["code"] == 0:
			return redirect('/login/')
		else:
			return render_template('register.html',result=result)
	return render_template('register.html')


# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method=="POST":
		data = {k:v[0] for k,v in dict(request.form).items()}
		result = utils.getone('user1',data,field)
		print data,result
		if result["code"] == 0: 
			if result['msg']['password'] == data['password']:
				session['username'] = data['username']
				session['role'] = result['msg']['role']
				if session['role'] == 0:
					return redirect('/userlist/')
				else:
					return redirect('/index/')
			else:
				result['msg'] = "password error"
				return render_template('login.html',result=result)
		else:
			result['msg'] = "user is not exit"
			return render_template('login.html',result=result)
	return render_template('login.html')

#注销
@app.route('/logout/')
def logout():
	session.clear()
	return redirect('/login/')


# 用户列表
@app.route('/userlist/')
def userlist():
	if not session or session['role'] != 0:
		return redirect('/login/')
	
	user = utils.userlist('user1')
	return render_template('list.html',user=user,info=session)


#用户信息
@app.route('/userinfo/')
def userinfo():
	if not session:
		return redirect('/login/')
	uid = request.args.get('id',"")
	data = {'id':uid}
	result = utils.getone('user1',data,field)
	if result['code'] == 0:
		result = result['msg']
	#return json.dumps(result)
	return render_template("update.html",result=result)


# 删除
@app.route('/delete/',methods=['GET','POST'])
def delete():
	if request.method=="GET":
		uid = request.args.get('id','')
		utils.delete('user1',uid)
		return redirect('/userlist/')
	return render_template('list.html')


# 更改
@app.route('/update/',methods=['GET','POST'])
def update():
	if request.method == 'POST':
        	data = dict(request.form)
        	data = {k:v[0] for k,v in data.items()}
        	result = utils.update('user1',field,data)
        	if result['code']==0:
               		return redirect("/userlist/")
        	else:
                	return render_template('update.html',result=result)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5555,debug=True)
