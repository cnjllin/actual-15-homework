#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template
import pymysql as mysql
app = Flask(__name__)

conn = mysql.connect(user='root',passwd='root',db='log',charset="utf8",host='127.0.0.1')
conn.autocommit(True)
cur = conn.cursor()

@app.route('/',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sql = 'select * from costomer where name=%s and password=md5(%s)'
        if cur.execute(sql,(username,password)):

            return "log in success"
        else:
            return "username or password is wrong"
    return  render_template('login.html')

@app.route('/logup/',methods=['GET', 'POST'])
def logup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            sql = 'insert into costomer (name,password) values ("%s",md5(%s))' %  (username,password)
            cur.execute(sql)
            return "%s log up successful"  % (username)
    return render_template('logup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
