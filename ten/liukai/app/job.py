#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
import utils
import json
import  util
import time
from . import app

###### 工单系统 ##############

table="ops_jobs"
field=['id','apply_date','apply_type','apply_desc','del_person','status','deal_desc','dela_time','apply_persion']

# 添加工单
@app.route("/jobadd/",methods=['GET','POST'])
def jobadd():
    if not session:
        return redirect("/")
    if request.method=='POST':
        job={k:v[0] for k,v in dict(request.form).items()}
        field=['apply_date','apply_type','apply_desc','status','apply_persion']
        job['apply_date']=time.strftime('%Y-%m-%d %H:%M')
        job['status']=0
        print 'job-->',job
        data=utils.insert(table,field,job)
        return json.dumps(data)
    return render_template("job_add.html",res=session)
    
# 申请列表表
@app.route("/joblist/",methods=['GET','POST'])
def joblist():
    if not session:
        return redirect("/")
    result=utils.list(table,field)
    data=result['msg']
    return render_template("joblist.html",data=data,res=session )

# 修改列表
@app.route("/jobupdate/",methods=['GET','POST'])
def jobupdate():
    if not session:
        return redirect("/")
    if request.method=="GET":
        id=request.args.get('id')
        data={}
        data['id']=int(id)
        data['del_person']=session['username']
        data['status']=1
        print 'data--->',data
        field=['id','del_person','status']
        result=utils.update(table,field,data)
        print "result-->",result
        return json.dumps(result)
    else:
        data={k:v[0] for k,v in dict(request.form).items()}
        data['del_person']=session['username']
        data['status']=2
        data['dela_time']=time.strftime('%Y-%m-%d %H:%M')
        field=['id','del_person','dela_time','deal_desc','status']
        result=utils.update(table,field,data)
        return json.dumps(result)
      
# 工单详情
@app.route('/jobdetail/',methods=["GET","POST"])
def jobdetail():
#    if session:
#        return redirect("/")
    if request.method=="GET":
        id=request.args.get("id")
        data={}
        data['id']=int(id)
        result=utils.get_one(table,field,data)
	result['msg']['apply_date']=str(result['msg']['apply_date'])
        result['msg']['dela_time']=str(result['msg']['dela_time'])
        print "result-->",result
        return json.dumps(result)

# 历史工单
@app.route("/jobhistory/",methods=['GET','POST'])
def jobhistory():
    if not session:
        return redirect("/")
    result=utils.list(table,field)
    data=result['msg']
    return render_template("jobhistory.html",data=data,res=session )

