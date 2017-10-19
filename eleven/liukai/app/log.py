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
        data={"data": [{"name": "200", "value": 115}, {"name": "404", "value": 300}, {"name": "502", "value": 250},{"name":"500","value":180},{"name":"301","value":80}], "legend": ["200", "404", "502","500","301"]}
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
    data={"code": 0, "result": [{"name":"台湾","value":1203},{"name":"山西","value":123},{"name":"香港","value":987},{"name":"澳门","value":2340},{"name": "福建", "value": 1930}, {"name": "贵州", "value": 6934}, {"name": "宁夏", "value": 115}, {"name": "广东", "value": 3940}, {"name": "重庆", "value": 1706}, {"name": "甘肃", "value": 7320}, {"name": "四川", "value": 6832}, {"name": "河南", "value": 2870}, {"name": "安徽", "value": 17}, {"name": "江苏", "value": 3046}, {"name": "湖南", "value": 651}, {"name": "北京", "value": 1667}, {"name": "新疆", "value": 393}, {"name": "浙江", "value": 1319}, {"name": "广西", "value": 138}, {"name": "青海", "value": 519}, {"name": "陕西", "value": 223}, {"name": "陕西", "value": 8671}, {"name": "黑龙江", "value": 10}, {"name": "西藏", "value": 255}, {"name": "海南", "value": 1139}, {"name": "天津", "value": 253}, {"name": "辽宁", "value": 796}, {"name": "江西", "value": 492}, {"name": "内蒙古", "value": 16}, {"name": "吉林", "value": 1955}, {"name": "河北", "value": 571}, {"name": "云南", "value": 2}, {"name": "山东", "value": 940}, {"name": "上海", "value": 1527}, {"name": "湖北", "value": 2914}]}
    return json.dumps(data)

