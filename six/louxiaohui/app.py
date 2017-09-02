#!/usr/bin/python
# -*- coding:utf-8 -*-
# **********************************************************
# * Author        : louxiaohui
# * Email         : 1031138448@qq.com
# * Last modified : 2017-08-14 00:58
# * Filename      : sample_flask.py
# * Description   : user_management_system
# * ********************************************************
from flask import Flask,request,render_template,redirect
from utils import create_user,convert_user_info_to_dict,update_user_info,delete_user_info,get_all_user_info,check_user_login
import MySQLdb as mysql
import hashlib
app = Flask(__name__)

# connect to mysql database
conn = mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')
# set autocommit to True to enable the insert happened successfully
conn.autocommit(True)
# create a cursor
cur = conn.cursor()
# index page
@app.route('/')
@app.route('/index/')
def index():
    return render_template("login.html")
# user registeration page
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_info_dict = dict(request.form)
        data = {k:v[0] for k,v in user_info_dict.iteritems()}
        print data
        create_user('user',data)
        res={'msg':'register successfully'}
        return render_template('susccess.html',res=res)
    res={'msg':''}
    return render_template('register.html',res=res)
# user login page
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        user_info_dict = dict(request.form)
        data = {k:v[0] for k,v in user_info_dict.iteritems()}
        if check_user_login('user',data):
            return redirect('/userlist')
        else:
            error = 'username or password is wrong'
            return render_template("login.html",error = error)
    return render_template("login.html")

# get information of all users
@app.route('/userlist',methods=['GET','POST'])
def userlist():
    user_data=get_all_user_info('user')
    return render_template('userlist.html',data=user_data)
# delete user
@app.route('/delete_user')
def delete_user():
    id = request.args.get('id')
    print id
    delete_user_info('user',id)
    return redirect('/userlist')
# update user information
@app.route('/update_user',methods=['GET','POST'])
def updateuser():
    res={}
    uid = request.args.get('id')
    print dict(request.args)
    print uid
    if request.method == 'POST':
        uid = request.form.get('id')
        print "uid:%s" %uid
        result = convert_user_info_to_dict('user',uid)
        user_info_dict = dict(request.form)
        data = {k:v[0] for k,v in user_info_dict.iteritems()}
        if update_user_info('user',data):
            res = {'msg':'profile update ok !','code':0}
            return render_template('update.html',res=res,uid=uid,data=result)
        else:
            res = {'msg':'profile update failed !','code':1}
            return render_template('update.html',res=res,uid=uid,data=result)
    result = convert_user_info_to_dict('user',uid)
    return render_template('update.html',res=res,uid=uid,data=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
