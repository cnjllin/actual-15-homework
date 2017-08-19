#!/bin/env python
#coding:utf-8

#导入相关模块
from flask import Flask,request,render_template
from judge import judge_user

#初始化列表和字典
data_list = []
dict1 = {}

app = Flask(__name__)

#后端注册，将用户名和密码保存到abc.txt文件
@app.route('/reg_back/',methods=["GET","POST"])
def reg():
    username = request.form.get('username')
    ret = judge_user(username)
    if ret ==0:
        passwd_first = request.form.get('passwd_first')
        passwd_second = request.form.get('passwd_second')
        if passwd_first == passwd_second:
            with open("abc.txt",'a+') as f:
                f.write("%s:%s\n" %(username,passwd_first) )
        return "hello world! name is %s,password is %s" %(username,passwd_first)
    else:
        return "user have exist"

#通过前端获取注册数据
@app.route('/reg/')
def index():
    return render_template("reg.html",result = res)

#通过前端获取登陆数据
@app.route('/login/',methods = ['GET','POST'])
def index1():
    return render_template("login.html")

#后端登陆，比对用户信息，并返回结果
@app.route('/login_back/',methods=["GET","POST"])
def login1():
    username = request.form.get('username')
    ret = judge_user(username)
    if ret == 1:
        password = request.form.get('password')
        with open("abc.txt",'a+') as f:
            for x in f:
                dict1[username] = x.rstrip("\n").split(":")[1]
            print dict1
        if password != dict1[username]:
            return "password is wrong!"
        else:
            return "login success!!"
    else:
        return "user is not exist!"
        
if __name__=='__main__':
    app.run(host='59.110.12.72',port=8888,debug=True)
