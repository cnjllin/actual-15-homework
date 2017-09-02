#!/usr/bin/python
#coding:utf-8

from flask import Flask,request,render_template,redirect

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

import MySQLdb as mysql
con=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot15',port=3306,charset='utf8')
con.autocommit(True)
cur = con.cursor()

import utils
table = "user"
app = Flask(__name__)

field = ['id','username','password','role']

#首页
@app.route('/')
@app.route('/index/')
def index():
    username = "欢迎登录工单系统"
    return render_template('index.html',username=username)

#注册页面
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method == "POST":
	data =  {k:v[0] for k,v in dict(request.form).items()}
        field = ['username','password','role']
        reg_user = utils.user_name(table,field,data['username'])
        if reg_user:
            msg = {'code':1,'errmsg':'user is already'}
            return render_template('reg.html',msg=msg) 
        else:
            utils.insert(table,field,data)
            return redirect('/login/')
    msg = {}
    return render_template('reg.html',msg=msg)


#登录页面
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == "POST":
        data = {k:v[0] for k,v in dict(request.form).items()}
        print data
        login_user = utils.user_name(table,field,data['username'])
        if data['username'] == login_user[1] and data['passwd'] == login_user[2]:
            res = dict(zip(field,login_user))
            userlist = utils.user_list(table,field)
            msg = {'code':0,'sucmsg':'login success'} 
            return render_template('info.html',msg=msg,user=res,userlist=userlist)
        else:
            msg = {'code':1,'errmsg':'user or passwd is wrong'}
            return render_template('login.html',msg=msg)
    msg={}
    return render_template('login.html',msg=msg)


#删除用户
@app.route('/dele/',methods=['GET','POST'])
def dele():
    if request.method == 'GET':
        uid = request.args.get('id')
        del_user = utils.dele(table,uid)
        return redirect('/info/')

#查询用户
@app.route('/info/',methods=['GET','POST'])
def select():
    if request.method == "GET":
        uid = request.args.get('id')
        res = utils.user_id(table,field,uid)
        return render_template('update.html',res=res)

#修改用户
@app.route('/update/',methods=['GET','POST'])
def update():
    if request.method == "POST":
        data = {k:v[0] for k,v in dict(request.form).items()}
        utils.update(table,field,data)
        return redirect('/login/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)

