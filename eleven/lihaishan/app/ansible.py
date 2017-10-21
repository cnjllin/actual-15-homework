#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
from utile import insert,getone,update,delete,list
import json
import util
from app import app
from datetime import datetime
from commands import ansiblecommand
server_fields = ['id','hostname']

@app.route("/ansible/",methods=["GET","POST"])
def ansilbe():
    if "username" not in session:
        return redirect("/login/")
    if request.method=="GET":
        server=list("server",server_fields)
        return render_template('ansible.html',server=server['msg'])

    if request.method=="POST":
        cmdmsg ={k:v[0] for k,v in dict(request.args).items()}
        #记录日志写入文件
        cmd_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cmd_history="Time:%s User:%s Host:%s Cmd :%s \n" %(cmd_time,session["username"],cmdmsg['pattern'],cmdmsg['cmd'])
        with open("/tmp/ansible.log",'a') as ansible_log:
            ansible_log.write(cmd_history)
            ansible_log.close

        ansiblecmd =ansiblecommand(cmdmsg["cmd"],cmdmsg["pattern"])
        pattern=cmdmsg["pattern"]
        result=ansiblecmd["contacted"][pattern]["stdout"]
        if result:
            ansible_cmd="host: %s | CMD: %s | success>> \n" %(cmdmsg["pattern"],cmdmsg["cmd"])
            ansible_msg= ansible_cmd + result
            results= ansible_msg.replace("\n,<br>")
            return json.dumps(results)


#ansible 历史记录
@app.route("/history/",methods=["GET","POST"])
def history():
    if "username" not in session:
        return redirect("/login/")
    if request.method=="GET":
        ansible_history=""
        with file("/tmp/ansible.log")  as f:
            for line in reversed(f.readlines()):
                ansible_history +=line+"</br>"
        f.close
    return json.dumps(ansible_history)
