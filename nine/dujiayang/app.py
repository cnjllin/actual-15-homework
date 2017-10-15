#!/usr/bin/env  python
#coding:utf8

from flask import Flask,render_template,request,redirect,session
from utils import insert,getone,getlist,update,delete,getwhere
import json,util
app = Flask(__name__)
app.secret_key="dsadfasfadsfasf"


field = ['id','username','password','email','phone','role']
idc_field = ['id','name','name_cn','address','adminer','phone']
cabinet_field = ['id','name','idc_id','u_num','power','phone']
server_field = ['id','name','ip','idc_id','cabinet','os','core_num','mem','disk']
order_field = ['id','apply_time','apply_person','apply_type','apply_desc','deal_time','deal_person','deal_desc','status']

# 首页--用户资料
@app.route("/")
@app.route("/index/")
def index():
    if not session:
        return redirect("/login")
    data = {'id':session['id']}
    #data = {'username':session['username']}
    print data
    result = getone('user',field,data)
    util.WriteLog("[redirect '/' 过来的]").info('getone--%s'%result['msg'])
    print "index--getone--result"
    print result
    return render_template("index.html",info=result['msg'])

# 用户添加
@app.route("/reg/",methods=['GET','POST'])
def reg():
    if request.method == "POST":
            data = { k:v[0] for k,v in dict(request.form).items()}
	    print "模态窗添加用户的用户信息"
	    print data
            util.WriteLog('[模态窗添加用户的用户信息]').info(data)
            field = ['username','password','email','phone','role']
            result = insert('user',field,data)
	    print "添加用户写完数据库返回的的用户信息"
	    print result
            util.WriteLog('[管理员添加用户完成返回]').info(result)
	    return json.dumps(result)

# 用户登录
@app.route("/login/",methods=['GET','POST'])
def login():
    if request.method == "POST":
            data = { k:v[0] for k,v in dict(request.form).items()}
	    print "login-data"
            print data
            util.WriteLog('[用户开始登录echo post-data]').info(data)
            result = getone('user',field,data)
            util.WriteLog('[用户登录echo result]').info(result)
	    print result
            if result['code'] == 0:
                 if result['msg']['password']==data['password']:
                     session['username'] = data['username']
                     session['role']=result['msg']['role']
                     session['id']=result['msg']['id']
                     print session 
                     if session['role']==0: 
                        return redirect('/userlist/')
                     else:
                        return redirect('/')
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
    util.WriteLog('[redirect /userlist/]').info('getlist--%s' %result)
    print "userlist-getlist"
    print result
    print '\n'
    print result['msg']
    if result['code'] == 0:
        result = result['msg']
    return render_template("userlist.html",result=result,info = session)


# 用户更新
@app.route('/update/',methods=['GET','POST'])
def modity():
     if not session:
        return redirect("/login")
     if request.method == 'POST':
        data = dict(request.form)
        print "data11111"
        print data
        data = {k:v[0] for k,v in data.items()}
        print "data2222"
        print data
        result = update('user',field,data)
        if result['code']==0:
               util.WriteLog('[管理员更新用户资料]').info(result)
               return redirect("/userlist/")
        else:
                 return render_template('update.html',result=result)
     else:
        uid = request.args.get('id','')
	data = {'id':uid}
        print "-----------------------管理员更新，get请求过来的form值"
        print data
        result = getone('user',field,data)
        print "-----------------------管理员更新完result"
        print result
        return render_template('update.html',result=result['msg'])

# 修改个人资料
@app.route('/upinfo/',methods=['GET','POST'])
def upinfos():
     if not session:
        return redirect("/login")
     if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).iteritems()}
	print "upinfo-post-data"
        print data
	if data.has_key('newpasswd'):
		data = {'id':data['id'],'password':data['newpasswd']}
		print data
        	result = update('user',field,data)
        	util.WriteLog('[自己修改密码完成返回]').info(result)
		return json.dumps(result)
        result = update('user',field,data)
        util.WriteLog('[自己更新个人资料完成返回]').info(result)
	return json.dumps(result)
	#return redirect('/index/')

# 删除用户 
@app.route('/delete/')
def deleteuser():
     if not session:
        return redirect("/login")
     if request.method == 'GET':
	uid = request.args.get('id','')
        result = delete('user',uid)
#	return json.dumps(result)
	return redirect('/userlist/')


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


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
#	if request.method == 'GET':
#		orderid = request.args.get('id','')
#		data = {}
#		data['id'],data['status'],data['deal_person'] = orderid,1,session['username']
#		print "\n"
#		print "deal----deal"
#		print data
#		field = ['id','status','deal_person']
#		result = update('work_order',field,data)
#		return json.dumps(result)
			#return redirect('/orderlist/',result=result,info=session)
	

## 工单历史
@app.route('/orderhistory/',methods=['GET','POST'])
def order_history():
	if request.method == 'GET':
		data = {'stat':1}
		result = getwhere('work_order',order_field,data)['msg']		
		return render_template('orderhistorylist.html',result=result,info=session)
	

			

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5566,debug=True)
