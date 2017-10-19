#! /usr/bin/env python
# _*_coding:utf-8_*_

from flask import Flask,render_template,request,redirect,session
import utils
import json
import  util
import time
from . import app
import ansible.runner as a

@app.route("/ansible/",methods=["GET","POST"])
def ansible():
    if not session:
       return redirect("/")
    return render_template("ansible.html",res=session)

@app.route("/ansible_hostname/")
def hostname():
     if not session:
        return redirect("/")
     result=[]
     data=a.Runner(module_name='shell',module_args='hostname',pattern='all',forks=5).run()
     for i in data['contacted']:
         result.append(i)
     return json.dumps(result)

@app.route("/ansible_data/",methods=["GET","POST"])
def data():
     if not session:
        return redirect("/")
     #res={k:v[0] for k,v in dict(request.get).itmes()}
     module=request.args.get('module')
     cmd=request.args.get('cmd')
     pattern=request.args.get('pattern')
     forks=request.args.get('forks')
     result=[]
     data=a.Runner(module_name=module,module_args=cmd,pattern=pattern,forks=forks).run()
     times=time.strftime('%Y-%m-%d %H:%M')
     log="%s-%s-%s-%s\n"%(times,session['username'],pattern,cmd)
     print log
     with open('/tmp/ansible.log','a+') as f: 
         f.write(log)
     #print data['contacted']
     for k,v in data['contacted'].items():
         time1=v['end']
         name=session['username']
         cmd=v['cmd']
         stdout=v['stdout']
         status=v['changed']
         result.append({'hostname':k,'time':time1,'name':name,'cmd':cmd,'status':status,'stdout':stdout})
     return json.dumps(result)


@app.route("/ansible_list/")
def ansible_list():
    if not session:
       return redirect("/")
    with open('/tmp/ansible.log','r') as f:
        data=f.readlines()
    return json.dumps(data)
