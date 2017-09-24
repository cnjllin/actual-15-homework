#!/bin/env python
#coding:utf8
# Author:changhuawei
# time:2017/9/23

from flask import Flask,request,render_template,redirect,session
from db import *
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')

app=Flask(__name__)
app.secret_key="daf"

field = ['id','username','password','role','email','phone','age'] 

# 主页面
@app.route('/')
@app.route('/index/')
def index():
	if not session:
		return redirect('/login')
	data={'username':session['username']}
	print data
	result = getone('user',field,data)
	print result
	return render_template('index.html',result=result['msg'])

# 用户注册
@app.route('/registor/',methods=['POST','GET'])
def registor():
	if request.method == 'POST':
		field = ['username','password','age','phone','email','role']
		data = {k:v[0] for k,v in dict(request.form).items()}
		print data
		result = insert('user',field,data)
		print result
		if result['code'] == 0:
			return redirect('/login/')
		else:
			return render_template('registor.html',result=result)
	return render_template('registor.html')

# 用户登录
@app.route('/login/',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).items()}
		#print data
		result = getone('user',field,data)
		#print result
		if result['code'] ==0:
			if result['msg']['password'] == data['password']:
				session['username'] = data['username']
				session['role'] = result['msg']['role']
			else:
				result['code']=1,
				result['errmsg']='wrong passwd'
			print session
		else:
			result['errmsg']='user is not exsit'
		return json.dumps(result)
	return render_template('login.html')

# 用户登录界面,普通用户只能看到个人信息，管理员可以看到用户列表
@app.route('/user/')
def user():
    if not session:
	return render_template('login.html')
    username=session['username']
    data={'username':username}
    result=getone('user',field,data)
    print result
    return render_template('index.html',res=session ,result=result['msg'])

# 管理员用户界面 
@app.route('/userlist/')
def userlist():
	if not session:
		return redirect('/login/')
	result = alllist('user',field)
	print result
	return render_template('userlist.html',result=result)

# 显示用户个人信息
@app.route('/userinfo/')
def userinfo():
	if not session:
		return redirect('/login/')
	uid = request.args.get('id')
	data = {'id':uid}
	print data
	result = getone('user',field,data)
	print result
	if result['code'] == 0:
		return json.dumps(result['msg'])

# 更改用户信息
@app.route('/update/',methods=['POST','GET'])
def update():
	if not session:
		return redirect('/login')
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).items()}
		result = modify('user',data)
                print result
		return json.dumps(result)

# 修改用户密码
@app.route('/updatepasswd/',methods=['POST','GET'])
def updatepasswd():
	if not session:
		return redirect('/login')
	if request.method == "POST":
		data={'password':request.form.get('password'),'id':request.form.get('id')}
		newpasswd=request.form.get('newpasswd')
		result = getone('user',field,data)
		if result['msg']['password'] == data['password']:
			data['password'] = newpasswd	
			result = modify('user',temp_dict)
		else:
			result['msg']="旧密码输入错误"
			result['code']=1
		return json.dumps(result)

# 删除用户
@app.route('/delete/')
def delete():
	if not session:
		return redirect('/login')
	uid = request.args.get('id')
	data = {'id':uid}
	result = deleteuser('user',data)
	print result
	return json.dumps(result)

# 增加用户信息
@app.route('/adduser/',methods=['GET','POST'])
def adduser():
	if request.method == 'POST':
		field = ['username','password','age','phone','email','role']
		data = {k:v[0] for k,v in dict(request.form).items()}
		print data
		result = insert('user',field,data)
		if result['code'] == 0:
			return json.dumps(result)

# +++++++++++++++
#  机房管理
idc_field = ['id','name','name_cn','address','adminer','phone']

# 机房所有信息
@app.route('/idclist/')
def idclist():
	if not session:
		return redirect('/login/')
	result = alllist('idc',idc_field)
	print result
	print result['msg']
	return render_template('idclist.html',result=result)

# 显示机房信息
@app.route('/idcinfo/')
def idcinfo():
	if not session:
		return redirect('/login/')
	idcid = request.args.get('id')
	data = {'id':idcid}
	print data
	result = getone('idc',idc_field,data)
	print result
	if result['code'] == 0:
		return json.dumps(result['msg'])

# 添加机房
@app.route('/idcadd/',methods=['GET','POST'])
def idcadd():
	if request.method == 'POST':
		idc_field = ['name','name_cn','address','adminer','phone']
		data = {k:v[0] for k,v in dict(request.form).items()}
		print data
		result = insert('idc',idc_field,data)
		return json.dumps(result)

# 更新机房
@app.route('/idcupdate/',methods=['POST','GET'])
def idcupdate():
	if not session:
		return redirect('/login')
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).items()}
		result = modify('idc',data)
		return json.dumps(result)

# 删除机房
@app.route('/idcdelete/')
def idcdelete():
	if not session:
		return redirect('/login/')
	idcid = request.args.get('id')
	data = {'id':idcid}
	result = deleteuser('idc',data)
	print result 
	return json.dumps(result)	

# +++++++++++++++
# 机柜管理
cabinet_field = ['id','name','idc_name','u_num','power']

# 机柜所有信息
@app.route('/cabinetlist/')
def cabinetlist():
	if not session:
		return redirect('/login/')
	result = alllist('cabinet',cabinet_field)
	print result
	return render_template('cabinetlist.html',result=result)

# 显示机柜信息
@app.route('/cabinetinfo/')
def cabinetinfo():
	if not session:
		return redirect('/login/')
	cabinetid = request.args.get('id')
	data = {'id':cabinetid}
	print data
	result = getone('cabinet',cabinet_field,data)
	print result
	if result['code'] == 0:
		return json.dumps(result['msg'])

# 添加机柜
@app.route('/cabinetadd/',methods=['GET','POST'])
def cabinetadd():
	if request.method == 'POST':
		cabinet_field = ['name','idc_name','u_num','power']
		data = {k:v[0] for k,v in dict(request.form).items()}
		print data
		result = insert('cabinet',cabinet_field,data)
		return json.dumps(result)

# 更新机房
@app.route('/cabinetupdate/',methods=['POST','GET'])
def cabinetupdate():
	if not session:
		return redirect('/login/')
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).items()}
		result = modify('cabinet',data)
		return json.dumps(result)

# 删除机房
@app.route('/cabinetdelete/')
def cabinetdelete():
	if not session:
		return redirect('/login/')
	cabinetid = request.args.get('id')
	data = {'id':cabinetid}
	result = deleteuser('cabinet',data)
	print result 
	return json.dumps(result)

# 添加机柜式选机房接口
@app.route('/idcdata/')
def idcdata():
    result=select('idc','name')
    print json.dumps(result)
    return json.dumps(result)

# +++++++++++++++
# 服务器管理

server_field = ['id','ip','mac','username','password','port','idc','cabinet','brand','cpu','memory','disk','system_type']
# 机柜所有信息
@app.route('/serverlist/')
def serverlist():
	if not session:
		return redirect('/login/')
	result = alllist('server',server_field)
	print result
	return render_template('serverlist.html',result=result)

# 显示机柜信息
@app.route('/serverinfo/')
def serverinfo():
	if not session:
		return redirect('/login/')
	serverid = request.args.get('id')
	data = {'id':serverid}
	print data
	result = getone('server',server_field,data)
	print result
	if result['code'] == 0:
		return json.dumps(result['msg'])

# 添加机柜
@app.route('/serveradd/',methods=['GET','POST'])
def serveradd():
	if request.method == 'POST':
		server_field = ['ip','mac','username','password','port','idc','cabinet','brand','cpu','memory','disk','system_type']
		data = {k:v[0] for k,v in dict(request.form).items()}
		print data
		result = insert('server',server_field,data)
		return json.dumps(result)
	return render_template("serveradd.html")
# 更新机房
@app.route('/serverupdate/',methods=['POST','GET'])
def serverupdate():
	if not session:
		return redirect('/login/')
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).items()}
		result = modify('server',data)
		return json.dumps(result)

# 删除服务器信息
@app.route('/serverdelete/')
def serverdelete():
	if not session:
		return redirect('/login/')
	serverid = request.args.get('id')
	data = {'id':serverid}
	result = deleteuser('server',data)
	print result 
	return json.dumps(result)

# 添加服务器时选机柜接口	
@app.route('/cabinetdata/')
def cabinetdata():
    result=select('cabinet','name')
    print json.dumps(result)
    return json.dumps(result)

# +++++++++++++++
# 工单管理

job_field = ['id','type','contents','applicant','assign_to','apply_time','complete_time','status']

# 工单列表主要显示没有处理的工单
@app.route('/joblist/')
def joblist():
	if not session:
		return redirect('/login/')
	result = alllist('job',job_field)
	print result
	return render_template('joblist.html',result=result)


# 申请工单	
@app.route('/jobadd/',methods=['GET','POST'])
def jobadd():
	if request.method == 'POST':
		job_field = ['type','contents','applicant','assign_to']
		data = {k:v[0] for k,v in dict(request.form).items()}
		print data
		result = insert('job',job_field,data)
		return json.dumps(result)
	return render_template("jobadd.html")

# 历史工单显示所有工单信息
@app.route('/jobhistory/')
def jobhistory():
	if not session:
		return redirect('/login/')
	result = alllist('job',job_field)
	print result
	return render_template('jobhistory.html',result=result)

# 工单详情
@app.route('/jobdetail/')
def jobdetail():
	if not session:
		return redirect('/login/')
	jobid = request.args.get('id')
	data = {'id':jobid}
	result = getone('job',job_field,data)
	result['msg']['apply_time']=str(result['msg']['apply_time'])
	result['msg']['complete_time']=str(result['msg']['complete_time'])
	print result
	if result['code'] == 0:
		return json.dumps(result)

# 登出系统
@app.route('/logout/')
def logout():
	session.clear()
	return redirect('/login')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8888,debug=True)


