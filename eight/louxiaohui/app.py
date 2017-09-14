#!/usr/bin/python
# -*- coding:utf-8 -*-
# **********************************************************
# * Author        : louxiaohui
# * Email         : 1031138448@qq.com
# * Last modified : 2017-09-23 15:37
# * Filename      : app.py
# * Description   : user management
# * ********************************************************
from flask import Flask,request,render_template,redirect,session
from utils import insert,getone,user_list,update,delete
import MySQLdb as mysql
import json

app = Flask(__name__)

app.secret_key = "abcdrefgg"

# connect to mysql database
conn = mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')
# set autocommit to True to enable the insert happened successfully
conn.autocommit(True)
# create a cursor
cur = conn.cursor()

field = ['id','username','password','role']

@app.route('/table/')
def table_page():
    return render_template("table.html")

#@app.route('/getone/')
#def getone():
#    user={'username':'wd','password':'123456'}
#    return json.dumps(user)

@app.route('/')
@app.route('/index/')
def index_page():
    if not session:
        return redirect("/login/")
    print session
    username = 'wd'
    return render_template("index.html",username=username)

@app.route('/reg/',methods=['GET','POST'])
def reg():
    result = {}
    if request.method == 'POST':
        request_dict =  dict(request.form)
        print request_dict
        user = {k:v[0] for k,v in request_dict.items()}
        print user
        field = ['username','password','role']
        result = insert('user1',field,user)
        if result['code'] == 0:
            return redirect('/login/')
        else:
            return render_template('reg.html',result=result)
    return render_template("reg.html",result=result)

# login function
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == "POST":
        data = { k:v[0] for k,v in dict(request.form).items() }
        #result = {'code':0,'msg':data}
        print data
        # define a dictionary named result_info to sign whether the user is legal or not
        result_info = {'code':0,'msg':data}
        result = getone('user1',field,data)
        if result['code'] == 0:
            if result['msg']['password'] == data['password']:
                session['username'] = data['username']
                session['role'] = result['msg']['role']
                print session
                #if session['role'] == 0:
                #    return redirect("/userlist/")
                #else:
                #    return redirect("/userlist/")
            else:
                result_info['code'] = 1
                result_info['errmsg']="user %(username)s exist,but password is wrong,pls try again." % data
                #return render_template("login.html",result=result)
        else:
            result_info['code'] = 1
            result_info['errmsg']="user %(username)s does not exist" % data
            #return render_template("login.html",result=result)
        return json.dumps(result_info)
    return render_template("login.html")

@app.route('/userlist/')
def userlist():
    if not session:
        return redirect("/login/")
    print session
    result = user_list('user1',field)
    if result['code'] == 0:
        result = result['msg']
    return render_template("userlist.html",result=result,info=session)

@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect("/login/")
    username = session['username']
    data = {'username':username}
    print data
    result = getone('user1',field,data)
    print result
    if result['code'] ==0:
        result = result['msg']
    #return json.dumps(result)
    print result
    return render_template("userinfo.html",result=result)

@app.route('/update/',methods=['GET','POST'])
def modify():
    if not session:
        return redirect("/login/")
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        result = update('user1',field,data)
        print result
        if result['code']==0:
            return redirect("/userlist/")
        else:
            return render_template('update.html',result=result)

@app.route('/add/',methods=['GET','POST'])
def add():
    result = {}
    if request.method == 'POST':
        request_dict =  dict(request.form)
        print request_dict
        user = {k:v[0] for k,v in request_dict.items()}
        print user
        field = ['username','password','role']
        result = insert('user1',field,user)
        if result['code'] == 0:
            return redirect('/add/')
        else:
            return render_template('add.html',result=result)
    return render_template("add.html",result=result)

@app.route('/delete/')
def delete_user():
    if not session:
        return redirect("/login/")
    data = {k:v[0] for k,v in dict(request.args).iteritems()}
    print data,data['id']
    delete('user1',data)
    return redirect('/userlist')

@app.route('/logout/')
def logout():
    if session:
        session.clear()
    print session
    return redirect("/login/")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
