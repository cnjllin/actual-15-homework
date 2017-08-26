#!/usr/bin/env python
#-*- coding:utf-8 -*-

#-----------------------------------
#     FileName: CMDB.py
#         Desc:
#       Author: xin.yao
#      Version:
#     CreatTime: 2017-08-25
# ----------------------------------

from flask import Flask,render_template,request,redirect
# from util import judge_user,add_user,delete_user,change_user,check_user
import MySQLdb as mysql
app = Flask(__name__)
conn=mysql.connect(host="127.0.0.1",user="root",passwd="",db="reboot15",port=3306,charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

@app.route('/')
@app.route('/index/')
def index():
    hello = "Welcome to SCM"
    return render_template("index.html",hello=hello)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            sql = 'insert  user_msg (username,password) values ("%s","%s")' %  (username,password)
            try:
                cur.execute(sql)
                return render_template("success.html",msg=username)
            except Exception, e:
                error = u"%s 用户已经存在，请用其他用户名注册" % (username)
                return render_template("register.html",error=error)
        else:
            error = u"%s 两次密码不一致" % (username)
            return render_template('register.html',error=error)
    return render_template('register.html')
    
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        sql = "select * from user_msg where username='%s' and password = password('%s')" %(username,passwd)
        if cur.execute(sql):
            return redirect('/userlist/')
        else:
            error = u'用户名或者密码错误，请核对!'
            return render_template('login.html',error = error)
    return render_template('login.html')

@app.route('/userlist/',methods=['GET','POST'])
def userlist():
    sql = 'select * from user_msg'
    cur.execute(sql)
    res = cur.fetchall()
    return render_template("userlist.html",result=res)

@app.route('/delete/')
def delete():
    if request.method=='GET':
        uid=request.args.get("id")
        userid = int(uid)
        sql = 'delete from user_msg where id=%d;'% (userid)
        if cur.execute(sql):
            return render_template('success.html',msg=userid)
    return render_template(delet_the_user.html)

@app.route('/update/',methods=['GET','POST'])
def update():
    if request.method=='GET':
        userid = request.args.get("id")
        return render_template('update.html',userid=userid)
        print userid
    if  request.method=='POST':
        password = request.form.get("password")
        userid  = request.form.get("id")
        sql = 'select * from user_msg where id=%s' %(userid)
        if cur.execute(sql):
            npassword = request.form.get('npassword')
            sql='update user_msg set password=%s where id=%s' % (npassword,userid)
            if cur.execute(sql):
                return render_template('success.html')
            else:
                error = u"更新失败" 
                return  render_template('update.html',error=error)
        else:
            error = u"旧密码错误，请重新检查！"    
            return  render_template('update.html',error=error)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=1234,debug=True)