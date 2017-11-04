#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
from app import app
import json,psutil
import time

result = []
# 获取内存使用率
def get_mem_usage():
    data = {}
    mem = psutil.virtual_memory()
    mem_total = mem.total
    mem_free = mem.free
    mem_buffer = mem.buffers 
    mem_cache = mem.cached
    used = round((mem_total-mem_free-mem_buffer-mem_cache)/round(mem_total,4)*100,2)
    data[int(time.time())] = [int(time.time())*1000,used]
    result.append(data)
    return result

@app.route('/monitor/')
def memdata():
    return render_template('monitor/memusage.html')

@app.route('/memdata/')
def monitor():
    result = get_mem_usage()
    data = {'data':[]}
    for mem in result:
        data['data'].append({'name':mem.keys()[0],'value':mem.values()[0]})
    return json.dumps(data)

