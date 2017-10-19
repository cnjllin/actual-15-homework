#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
import utils
import json
import time
from . import app
import MySQLdb
import config
db=MySQLdb.connect(host=config.host,
                   user=config.user,
                   passwd=config.passwd,
                   db=config.db,
                   port=config.port,
                   charset=config.charset)
cur=db.cursor()
db.autocommit(True)





@app.route("/monitor/")
def mem():
    if not session:
        return redirect("/")
    return render_template("mem.html",res=session)

@app.route("/memdata/")
def memdata():
    lasttime=request.args.get('lasttime')
    sql='select * from mem'
    if lasttime:
        sql += ' where time>%s'%(lasttime)
    print sql
    cur.execute(sql)
    result=[]
    data={}
    for c in cur.fetchall():
        print c
        result.append({'name':c[1],'value':[c[1],c[0]]})
    data['data']=result
    data['lasttime']=result[-1]["name"]
    print data
    return json.dumps(data)
