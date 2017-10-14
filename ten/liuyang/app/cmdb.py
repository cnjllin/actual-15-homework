#!/bin/env python
#coding:utf8
# Author:liuyang
# create time:2017/8/17

from flask import request,render_template,redirect,session
from . import app
from db import *
import sys
import json
import time
reload(sys)
sys.setdefaultencoding('utf8')


# user表
field = ['id','username','password','age','phone','email','role'] 

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
		print data
		result = getone('user',field,data)
		print result
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
	return json.dumps(result)

# 增加用户信息
@app.route('/adduser/',methods=['GET','POST'])
def adduser():
	if request.method == 'POST':
		field = ['username','password','age','phone','email','role']
		data = {k:v[0] for k,v in dict(request.form).items()}
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
	return render_template('idclist.html',result=result)

# 显示机房信息
@app.route('/idcinfo/')
def idcinfo():
	if not session:
		return redirect('/login/')
	idcid = request.args.get('id')
	data = {'id':idcid}
	result = getone('idc',idc_field,data)
	if result['code'] == 0:
		return json.dumps(result['msg'])

# 添加机房
@app.route('/idcadd/',methods=['GET','POST'])
def idcadd():
	if request.method == 'POST':
		idc_field = ['name','name_cn','address','adminer','phone']
		data = {k:v[0] for k,v in dict(request.form).items()}
		#print data
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
	return json.dumps(result)	

# +++++++++++++++
# 机柜管理
cabinet_field = ['id','name','idc_id','u_num','power']

# 机柜所有信息
@app.route('/cabinetlist/')
def cabinetlist():
	if not session:
		return redirect('/login/')
	idcs = alllist('idc',idc_field)['msg']
	idc = {"%s"%idc['id']:idc['name'] for idc in idcs}
	cab = alllist('cabinet',cabinet_field)['msg']
	for c in cab:
		if c['idc_id'] in idc:
			c['idc_id'] = idc[c['idc_id']]
	return render_template('cabinetlist.html',result=cab,idc=idcs)

# 显示机柜信息
@app.route('/cabinetinfo/')
def cabinetinfo():
	if not session:
		return redirect('/login/')
	cabinetid = request.args.get('id')
	data = {'id':cabinetid}
	result = getone('cabinet',cabinet_field,data)
	if result['code'] == 0:
		return json.dumps(result['msg'])

# 添加机柜
@app.route('/cabinetadd/',methods=['GET','POST'])
def cabinetadd():
	if request.method == 'POST':
		cabinet_field = ['name','idc_id','u_num','power']
		data = {k:v[0] for k,v in dict(request.form).items()}
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
	#print result 
	return json.dumps(result)

# 添加机柜式选机房接口
@app.route('/idcdata/')
def idcdata():
    result=select('idc','name')
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
	return render_template('serverlist.html',result=result)

# 显示机柜信息
@app.route('/serverinfo/')
def serverinfo():
	if not session:
		return redirect('/login/')
	serverid = request.args.get('id')
	data = {'id':serverid}
	result = getone('server',server_field,data)
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
	return json.dumps(result)

# 添加服务器时选机柜接口	
@app.route('/cabinetdata/')
def cabinetdata():
    result=select('cabinet','name')
    return json.dumps(result)

# +++++++++++++++
# 工单管理

job_field = ['id','apply_type','apply_desc','apply_persion','deal_persion','apply_date','deal_time','deal_desc','status']

# 工单列表主要申请的工单
@app.route('/joblist/')
def joblist():
	if not session.get('username',None):
		return redirect('/login/')
	where = {'status':['0','1']}
	result = alllist('job',job_field)
	return render_template('joblist.html',result=result)

# 申请工单	
@app.route('/jobadd/',methods=['GET','POST'])
def jobadd():
	if not session.get('username',None):
		return redirect('/login/')
	if request.method == 'POST':
		job_field = ['apply_date','apply_type','apply_desc','status','apply_persion']
		data = {k:v[0] for k,v in dict(request.form).items()}
		if not data['apply_desc']:
			return json.dumps({'code':1,'msg':'job desc not null'})
		data['apply_date'] = time.strftime('%Y-%m-%d %H:%M')
		data['status'],data['apply_persion'] = 0,session['username']
		result = insert('job',job_field,data)
		return json.dumps(result)
	else:
		return render_template('jobadd.html',result = session)

# 工单处理
@app.route('/jobupdate/',methods=['GET','POST'])
def jobupdate():
	if not session.get('username',None):
		return redirect('/login')
	name = session['username']
	if request.method == "POST":
		data = {k:v[0] for k,v in dict(request.form).items()}
		data['status'] = 2
		data['deal_persion'] = name
		data['deal_time'] = time.strftime('%Y-%m-%d %H:%M')
		print data
		result = modify('job',data)
	else:
		id =request.args.get('id')
		data = {'id':id,'status':1,'deal_persion':name,'deal_time':time.strftime('%Y-%m-%d %H:%M')}
		result = modify('job',data)
	return json.dumps(result)

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
	result['msg']['apply_date']=str(result['msg']['apply_date'])
	result['msg']['deal_time']=str(result['msg']['deal_time'])
	print result
	if result['code'] == 0:
		return json.dumps(result)

# 登出系统
@app.route('/logout/')
def logout():
	session.clear()
	return redirect('/login')




