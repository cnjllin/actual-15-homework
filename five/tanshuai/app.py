#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/8/14日14点34分

from flask import Flask, render_template, request, redirect
import user

# flask框架定义（实例化）
app = Flask(__name__)

# 网站首页
@app.route('/')
def index():
    # 首页：选择登录还是注册
    return render_template('index.html')
    # return 'hello, Flask!'

'''用户列表模块
'''
@app.route('/user/list/')
def userlist():
    sql = "select * from user"
    user_list = user.GetUser(sql)
    return render_template('userlist.html', user_list=user_list)

'''用户登录模块
'''
@app.route('/user/login/', methods=['POST','GET'])
def logined():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username', None)
    password = params.get('password', None)

    if request.method == 'GET':
        return render_template('login.html')
    else:
        if user.ValidateLogin(username, password):
            print (username, password)
            return redirect('/user/list/')
        else:
            print '登录失败'
            return render_template('login.html', username=username, error=u'用户名或密码错误')

'''创建用户模块
'''
@app.route('/user/create/', methods=['POST', 'GET'])
def created():
    params = request.args if request.method == 'GET' else request.form
    username = params.get('username', None)
    password = params.get('password', '')
    sex = params.get('sex', None)
    age = params.get('age', None)
    phone = params.get('phone', None)
    email = params.get('email', None)
    role = params.get('role', None)

    if request.method == 'GET':
        return render_template('adduser.html')
    else:
        if user.ValidateUser(username):
            return render_template('adduser.html', error=u'用户名已存在')
        if password == '':
            return render_template('adduser.html', error=u'密码不能为空')

        args = (username,password,sex,age,phone,email,role)
        print args
        if user.UserAdd(args):
            return redirect('/user/list/')
        else:
            return render_template('adduser.html', error=u'用户添加失败')


'''更新用户模块
'''
@app.route('/user/update/', methods=['POST', 'GET'])
def update():
    params = request.args if request.method == 'GET' else request.form
    uid = params.get('uid', '')
    password = params.get('password', '')
    sex = params.get('sex', None)
    age = params.get('age', None)
    phone = params.get('phone', None)
    email = params.get('email', None)
    role = params.get('role', None)

    # 查询出数据，post和get方法共用
    sql = 'select * from user where id= %s' % uid
    rt_user = user.GetUser(sql)[0]

    if request.method == 'GET':
        return render_template('userupdate.html', user=rt_user)
    else:
        if password == '':
            return render_template('userupdate.html', user=rt_user, error=u'密码不能为空')
        args = (password,sex,age,phone,email,role,uid)
        print args
        if user.UserUpdate(args):
            return redirect('/user/list/')
        else:
            return render_template('userupdate.html', error=u'更新添加失败')

"""删除用户信息
"""
@app.route('/user/delete/')
def DeleteUser():
    params = request.args if request.method == 'GET' else request.form
    uid = params.get('uid', '')
    if user.UserDelete(uid=(uid,)):
        return redirect('/user/list/')
    else:
        print '删除用户失败！'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

