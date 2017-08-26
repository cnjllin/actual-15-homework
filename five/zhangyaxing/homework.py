#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template
import pymysql as mysql
app = Flask(__name__)

conn = mysql.connect(user='root',passwd='root',db='db',charset="utf8",host='127.0.0.1')
conn.autocommit(True)
cur = conn.cursor()

# log in
@app.route('/',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sql = 'select * from user where username=%s and password=%s'
        if cur.execute(sql,(username,password)):
            return "log in successfully"
        else:
            return "username or password is wrong"
    return  render_template('login.html')

# log up
@app.route('/logup/',methods=['GET', 'POST'])
def logup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            sql = 'insert into user (username,password) values ("%s","%s")' %  (username,password)
            cur.execute(sql)
            return "%s log up successfully"  % (username)
    return render_template('logup.html')

# user list
@app.route("/userlist/",methods=["GET","POST"])
def userlist():
    sql = 'select * from user'
    cur.execute(sql)
    res = cur.fetchall()
    print res
    return render_template("userlist.html",result=res)

# delete user
@app.route("/del/",methods=['GET','POST'])
def delete_user():
    if request.method == 'GET':
        userid = int(request.args.get('id'))
        sql = 'delete from user where id=%d' % (userid)
        cur.execute(sql)
    return render_template('userlist.html')

# update user
@app.route("/update/",methods=['GET','POST'])
def update_user():
    if request.method == 'GET':
        userid = int(request.args.get('id'))
        return render_template("update.html",userid=userid)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        userid = request.form.get('id')
        if password == repassword:
            sql = 'update user set password=%s where id=%s' % (password,userid)
            cur.execute(sql)
            return render_template("userlist.html")
        return render_template("userlist.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
