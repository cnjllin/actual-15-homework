#!/usr/bin/python
#coding:utf-8

from flask import render_template,redirect,request,session,url_for
from exts import db,app
from utils import *

db.create_all()

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        user_info = user_dict(request.form)
        if  user_check(user_info['user_name']):
            error = 'Invalid user!'
        else:
            user_pass = user_info['user_pass']
            user_select = user_get(**user_info)
            if user_pass == user_select.user_pass:
                session['user_id'] = user_select.user_id
                if user_select.user_role == 0:
                    return render_template('member.html',user_select=user_select)
                else:
                    users_info = user_all()
                    return render_template('admin.html',users_info=users_info)
            else:
                error = 'Invalid Password!'
    return render_template('login.html',error=error)

# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    error = ''
    if request.method == 'POST':
        user_info = user_dict(request.form)
        if user_check(user_info['user_name']):
            if passwd_check(user_info):
                user_add(**user_info)
                return redirect(url_for('login'))
            else:
                error = 'Password Error!'
        else:
            error = 'the user exits!'
    return render_template('reg.html',error=error)

# 更新
@app.route('/update/int:<id>',methods=['GET','POST'])
def user_up(id):
    if session.get('user_id'):
        error = ''
        user_select = user_get(user_id=id)
        old_name = user_select.user_name
        if request.method == 'POST':
            user_info = user_dict(request.form)
            new_name = user_info['user_name']
            if not user_check(new_name) and new_name != old_name:
                error = "the user exits! "
            else:
                if passwd_check(user_info):
                    user_update(id,**user_info)
                    users_info = user_all()
                    return render_template('admin.html',users_info=users_info)
                else:
                    error = "Password Error!"
        return render_template('update.html',user_info=user_select,error=error)
    else:
        return redirect(url_for('index'))

# 删除
@app.route('/delete/')
def user_del():
    if session.get('user_id'):
        user_id = request.args.get('id')
        user_delete(user_id)
        users_info = user_all()
        return render_template('admin.html',users_info=users_info)
    else:
        return redirect(url_for('index'))

# 首页
@app.route('/index/')
def index():
    if session.get('user_id'):
        session.clear()
    return render_template('login.html')


if __name__=='__main__':
    app.run(host='0.0.0.0')
