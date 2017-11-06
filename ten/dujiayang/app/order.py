#!/usr/bin/env  python
#coding:utf8

from flask import Flask,render_template,request,redirect,session
from utils import insert,getone,getlist,getwhere,update,delete
import util
import json
from . import app
#app.secret_key="dsadfasfadsfasf"



order_field = ['id','apply_time','apply_person','apply_type','apply_desc','deal_time','deal_person','deal_desc','status']

## 工单管理
## 工单申请
@app.route('/orderapply/',methods=['GET','POST'])
def order_add():
	if request.method == 'POST':
		print session
		data = {k:v[0] for k,v in dict(request.form).iteritems()}
		data['apply_person'] = session['username']
		print data
		field = ['apply_type','apply_desc','apply_person']
		result = insert('work_order',field,data)
		if result['code'] == 0:
			result = {'code':0,'msg':'order is ok'}
			return json.dumps(result)
		else:
			result = {'code':1,'errormsg':'order is fail'}
			return json.dumps(result)
	if request.method == 'GET':
		return render_template('order_add.html',info=session)

## 工单列表
@app.route('/orderlist/',methods=['GET','POST'])
def order_list():
	if request.method == 'GET':
		result = getlist('work_order',order_field)
		if result['code'] == 0:
			result = result['msg']
			print "\n"
			print result
			for i in result:
				print i
				if int(i['status']) == 0:
					print i['status']
					i['status'] = "doing"
				else:
					i['status'] = "done"
		return render_template('order_list.html',result=result,info=session)

## 工单处理
@app.route('/orderdeal/',methods=['GET','POST'])
def order_deal():
	if request.method == 'POST':
		data = {k:v[0] for k,v in dict(request.form).iteritems()}
		print '111111111111111111data'
		print data
		data['status'],data['deal_person'] = 1,session['username']
		print '\n'
		print data
		field = ['status','deal_person','deal_desc']
		result = update('work_order',field,data)
	#	if result['code'] == 0:
		return json.dumps(result)
#			result = result['msg']
#			return redirect('/orderlist/',result=result,info=session)
#		result = {'errmsg':'deal is fail'}
#		return render_template('order_list.html',result=result)
	if request.method == 'GET':
		orderid = request.args.get('id','')
		orderdesc = request.args.get('deal_desc','')
		data = {}
		data['id'],data['deal_desc'],data['status'],data['deal_person'] = orderid,orderdesc,1,session['username']
		print "\n"
		print "deal----deal"
		print data
		field = ['id','deal_desc','status','deal_person']
		result = update('work_order',field,data)
		return json.dumps(result)
			#return redirect('/orderlist/',result=result,info=session)


## 工单历史
@app.route('/orderhistory/',methods=['GET','POST'])
def order_history():
	if request.method == 'GET':
		data = {'stat':1}
		result = getwhere('work_order',order_field,data)['msg']
		return render_template('orderhistorylist.html',result=result,info=session)
