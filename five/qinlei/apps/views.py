#coding: utf-8
from flask import render_template,request,session,redirect,flash,url_for
from apps import app
import json
import db


@app.route('/')
@app.route('/index/')
def index():
    #print session.get('logged_in')
    if session.get('logged_in'):
        return render_template("base.html")
    else:
        return redirect('login')


@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':

        '''data：post提交的用户与密码,生成一个字典'''
        data = dict((k, v[0]) for k, v in dict(request.form).items())


        '''sql_user:数据库用户,密码，生成一个列表'''
        sql_user = [(x['username'],x['password'],x['role']) for x in db.query('users', app.config.get('FIELDS'))]


        '''user: 数据库用户、密码转换成字典格式'''
        user = { x[0]:[x[1],x[2]] for x in sql_user }

        if data['username'] not in sql_user and data['password'] == user[data['username']][0]:
            session['logged_in'] = True
            session['username'] = data['username']
            session['role'] = user[data['username']][1]
            return redirect('index')

        else:
            return redirect('login')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You were logged out')
    return redirect(url_for('login'))