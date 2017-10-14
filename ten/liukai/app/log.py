#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
import utils
import json
import  util
import time
from . import app



# 饼状图
@app.route("/log/",methods=["GET","POST"])
def log():
    if not session:
        return redirect("/")
    return render_template("log.html",res=session)


@app.route("/status/",methods=["GET","POST"])
def status():
    if request.method=="GET":
        data={"data": [{"name": "200", "value": 234}, {"name": "404", "value": 300}, {"name": "502", "value": 250},{"name":"500","value":310}], "legend": ["200", "404", "502","500"]}
        return json.dumps(data)

@app.route("/map/")
def map():
    if not session:
        return redirect("/")
    return render_template("map.html",res=session)


@app.route("/mapdata/")
def mapdata():
    if not session:
        return redirect("/")
    data={"code": 0, "result": [{"name": "\u798f\u5efa", "value": 1930}, {"name": "\u8d35\u5dde", "value": 6934}, {"name": "\u5b81\u590f", "value": 115}, {"name": "\u5e7f\u4e1c", "value": 3940}, {"name": "\u91cd\u5e86", "value": 1706}, {"name": "\u7518\u8083", "value": 7320}, {"name": "\u56db\u5ddd", "value": 6832}, {"name": "\u6cb3\u5357", "value": 2870}, {"name": "\u5b89\u5fbd", "value": 17}, {"name": "\u6c5f\u82cf", "value": 3046}, {"name": "\u6e56\u5357", "value": 651}, {"name": "\u5317\u4eac", "value": 1667}, {"name": "\u65b0\u7586", "value": 393}, {"name": "\u6d59\u6c5f", "value": 1319}, {"name": "\u5e7f\u897f", "value": 138}, {"name": "\u9752\u6d77", "value": 519}, {"name": "\u9655\u897f", "value": 223}, {"name": "\u5c71\u897f", "value": 8671}, {"name": "\u9ed1\u9f99\u6c5f", "value": 10}, {"name": "\u897f\u85cf", "value": 255}, {"name": "\u6d77\u5357", "value": 1139}, {"name": "\u5929\u6d25", "value": 253}, {"name": "\u8fbd\u5b81", "value": 796}, {"name": "\u6c5f\u897f", "value": 492}, {"name": "\u5185\u8499\u53e4", "value": 16}, {"name": "\u5409\u6797", "value": 1955}, {"name": "\u6cb3\u5317", "value": 571}, {"name": "\u4e91\u5357", "value": 2}, {"name": "\u5c71\u4e1c", "value": 940}, {"name": "\u4e0a\u6d77", "value": 1527}, {"name": "\u6e56\u5317", "value": 2914}]}
    return json.dumps(data)
