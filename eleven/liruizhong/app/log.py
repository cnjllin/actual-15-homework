#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
from app import app
import json,psutil
import time

#日志
@app.route('/log/',methods=['GET', 'POST'])
def log():
    if 'name' not in  session:
        return redirect('/login/')
    if request.method=='GET':
        return render_template('log/log.html')

#日志状态数据
@app.route('/status/',methods=['GET','POST'])
def status():
    if 'name' not in  session:
        return redirect('/login/')
    if request.method=='GET':
        field=["200","304","404","206","301","403"]
        #result = logs('log',field)
        #return json.dumps(result)
        result = {'legend':"['200','302','404','500','502']",'data':"[{value:335, name:'502'}]"}
        return  json.dumps(result)
