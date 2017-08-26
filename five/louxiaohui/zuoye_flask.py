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
import MySQLdb as mysql
app = Flask(__name__)

# connect to mysql database
conn = mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')

# set autocommit to True to enable the insert happened successfully
conn.autocommit(True)
# create a cursor
cur = conn.cursor()
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_dict = {}
        user_info_list=['username','password','sex','age','phone','email','role']
        user_info = ",".join(user_info_list)
        table_list = ['username','passwd','gender','age','phone','email','role']
        user_dict = {}
        for i in table_list:
            user_dict[i] = request.form.get(i)
        print user_dict
        #username = request.form.get('username')
        #print username
        value = "'%s', password('%s'), %s, %s, '%s', '%s', %s" %(user_dict['username'],user_dict['passwd'],user_dict['gender'],user_dict['age'],user_dict['phone'],user_dict['email'],user_dict['role'])
        print value
        sql = "insert into user(%s) values (%s)" %(user_info,value)
        cur.execute(sql)
        res={'msg':'register successfully'}
        return render_template('susccess.html',res=res)
    res={'msg':''}
    return render_template('register.html',res=res)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("login.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        sql = "select * from user where username = '%s' and password = password('%s')" %(username,passwd)
        if cur.execute(sql):
            return redirect('/userlist')
        else:
            error = 'username or password is wrong'
            return render_template("login.html",error = error)
    return render_template("login.html")

@app.route('/userlist',methods=['GET','POST'])
def userlist():
    sql = 'select * from user'
    if cur.execute(sql):
        user_data=cur.fetchall()
        return render_template('userlist.html',data=user_data)

@app.route('/delete_user')
def delete_user():
    id = request.args.get('id')
    sql = 'delete from user where id = %s' %id
    cur.execute(sql)
    return redirect('/userlist')

@app.route('/update_user',methods=['GET','POST'])
def updateuser():
    res={'msg':''}
    if request.method == 'POST':
        uid = request.args.get('id')
        print "uid:%s" %uid
        password = request.form.get('password')
        repwd = request.form.get('repwd')
        print uid,password,repwd
        res = {'msg':''}
        if password == repwd:
            sql = "update user set password = password('%s') where id = %s" %(password,uid)
            print sql
            cur.execute(sql)
            res['msg']='Password update ok !'
            return render_template('update.html',res=res,uid=uid)
        else:
            res['msg']='Password not match !'
            return render_template('update.html',res=res,uid=uid)
    uid = request.args.get('id')
    print uid
    return render_template('update.html',res=res,uid=uid)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
