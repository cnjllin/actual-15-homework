# Author: tailorYang
from flask import render_template,request,redirect,session
from . import app
import config
import json
import db
import time

ISOTIMEFORMAT='%Y-%m-%d %X'

@app.route('/joblist/')
def joblist():
    role = session.get('role')
    res = db.select('ops_jobs')
    jobs = [dict((v,server[k]) for k,v in enumerate(config.job_fields)) for server in res]
    list_jobs = []
    for job in jobs:
        if job['status'] == 0 or job['status'] == 1:
	        list_jobs.append(job)
    return render_template("/job/joblist.html",jobs = list_jobs,role = role)

@app.route('/jobhistory/')
def jobhistory():
    role = session.get('role')
    jobs = db.select('ops_jobs')
    jobs = [dict((v,server[k]) for k,v in enumerate(config.job_fields)) for server in jobs]
    history_jobs = []
    for job in jobs:
        if job['status'] == 2 or job['status'] == 3:
    	    history_jobs.append(job)
    return render_template("/job/jobhistory.html",jobs = history_jobs,role = role)


@app.route("/jobadd/",methods=['GET','POST'])
def jobadd():
    name = session['username']
    print(name)
    id = session.get('id')
    if request.method == 'GET':
	    return render_template('/job/jobadd.html',info = session,role = session.get('role'))
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        data['apply_persion'] = name
        if not data['apply_desc']:
            return json.dumps({'code':1,'errmsg':'job description can not be null'})
        db.add('ops_jobs',data)
        return json.dumps({'code':0,'result':'apply job success'})

@app.route('/job_status/')
def job_status():
    id = request.args.get('id')
    job = db.select('ops_jobs',id=id)[0]
    job = {v: job[k] for k, v in enumerate(config.job_fields)}
    result1 = job['status']
    result2 = job['apply_desc']
    result3 = job['deal_desc']
    return json.dumps({'code':0,'result1':result1,'result2':result2,'result3':result3})

@app.route('/update_status/',methods=['POST'])
def update_status():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    print(data)
    conditions = [ "%s='%s'" %  (k,v) for k,v in data.items()]
    db.update('ops_jobs',conditions,data['id'])
    return json.dumps({'code':0,'result':'execute completed!'})
