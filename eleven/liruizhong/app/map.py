#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import maps
from app import app
import json

# 地图展示
@app.route('/map/',methods=['GET', 'POST'])
def map():
    if 'name' not in  session:
        return redirect('/login/')
    if request.method=='GET':
        return render_template('map/map.html')

#日志状态数据
@app.route('/mapdata/',methods=['GET','POST'])
def mapdata():
    if 'name' not in  session:
        return redirect('/login/')
    if request.method=='GET':
        result = maps('map')
        return  json.dumps(result)
