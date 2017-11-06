#!/usr/bin/env  python
#coding:utf8

from flask import Flask,render_template,request,redirect,session
from utils import insert,getone,getlist,getwhere,update,delete
import util
import json
from . import app
#app.secret_key="dsadfasfadsfasf"




idc_field = ['id','name','name_cn','address','adminer','phone']
cabinet_field = ['id','name','idc_id','u_num','power','phone']
server_field = ['id','name','ip','idc_id','cabinet','os','core_num','mem','disk']

## 机房管理
@app.route('/idc/')
def idclist():
	if not session:
		return redirect('/login/')
	result = getlist('newidc',idc_field)
	print result
	result = result['msg']
	return render_template("idc_list.html",result=result,info = session)

## 机房更新
@app.route('/idc_update/',methods = ['GET','POST'])
def idcmodify():
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).iteritems()}
		result = update('newidc',idc_field,data)
		if result['code'] == 0:
			return redirect('/idc/')
     	else:
	        IDCid = request.args.get('id','')
		data = {'id':IDCid}
	        result = getone('newidc',idc_field,data)['msg']
	        return render_template('idc_update.html',result=result)

## 机柜管理
@app.route('/cabinet/')
def cabinetlist():
	if not session:
		return redirect('/login/')
	idcs = getlist('newidc',idc_field)['msg']
#	idcs = {idc['id']:idc['name'] for idc in idcs}
	idcs = dict((idc['id'],idc['name_cn']) for idc in idcs)
	print "idcs-------idcs"
	print idcs
	cabinets = getlist('cabinet',cabinet_field)['msg']
	print "cabinets ---list--------------"
	print cabinets
	for i in cabinets:
		if int(i['idc_id']) in idcs:
			i['idc_id'] = idcs[int(i['idc_id'])]
	print "newnew-----newcabinets"
	print cabinets
	return render_template("cabinet_list.html",result=cabinets)


## 机柜更新
@app.route('/cabinet_update/',methods = ['GET','POST'])
def cabinetmodify():
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).iteritems()}
		result = update('cabinet',cabinet_field,data)
		if result['code'] == 0:
			return redirect('/cabinet/')
     	else:
	        IDCid = request.args.get('id','')
		data = {'id':IDCid}
	        result = getone('cabinet',cabinet_field,data)['msg']
	        return render_template('cabinet_update.html',result=result)


## 服务器管理
@app.route('/server/')
def serverlist():
	if not session:
		return redirect('/login/')
	idcs = getlist('newidc',idc_field)['msg']
	idcs = dict((idc['id'],idc['name_cn']) for idc in idcs)
	print "idcs-------idcs"
	print idcs
	servers = getlist('server',server_field)['msg']
	print "servers ---list--------------"
	print servers
	for i in servers:
		if i['idc_id'] in idcs:
			i['idc_id'] = idcs[i['idc_id']]
	print "newnew-----newservers"
	print servers
	return render_template("server_list.html",result=servers,info=session)
## 服务器add
@app.route('/AddServer/api/',methods=['GET','POST'])
def addserver():
    if request.method == "POST":
            data = { k:v[0] for k,v in dict(request.form).items()}
	    print "模态窗添加server的信息"
	    print data
            util.WriteLog('[模态窗添加server信息]').info(data)
            field = ['name','ip','idc_id','cabinet','os','core_num','mem','disk']
            result = insert('server',field,data)
	    print "添加server写完数据库返回的的用户信息"
	    print result
            util.WriteLog('[管理员添加server完成返回]').info(result)
	    return json.dumps(result)

## 服务器更新
@app.route('/server_update/',methods = ['GET','POST'])
def servermodify():
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).iteritems()}
		result = update('server',server_field,data)
		if result['code'] == 0:
			return redirect('/server/')
     	else:
	        serverid = request.args.get('id','')
		data = {'id':serverid}
	        result = getone('server',server_field,data)['msg']
	        return render_template('server_update.html',result=result)
