#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/8/14日14点34分

from flask import Flask, render_template, request, redirect, session
import os
import user
import json

# flask框架定义（实例化）
app = Flask(__name__)

# session_key定义
app.secret_key = os.urandom(32)
app.secret_key = '123123VASKFN2I3FPK1'

# 网站首页
@app.route('/')
def index():
    if session:
        return render_template('public/index.html')
    else:
        return redirect('/user/login/')

'''用户列表模块
'''
@app.route('/user/list/')
def userlist():
    sql = "select * from user"
    user_list = user.GetUser(sql)
    return render_template('user/user_list.html', user_list=user_list)

'''用户登录模块
'''
@app.route('/user/login/', methods=['POST','GET'])
def logined():
    if request.method == 'GET':
        return render_template('user/login.html')
    else:
        # 获取前端通过POST传进来的数据，通过列表生成式处理成字典
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        status, user_list = user.ValidateLogin(data['username'], data['password'])
        if status:
            session['username'] = user_list[0][1]
            session['role'] = user_list[0][7]
            if session['role'] == 0:
                return redirect('/user/list/')
            else:
                return render_template('index.html')
        else:
            print '登录失败'
            return render_template('user/login.html', username=data['username'], error=u'用户名或密码错误')

'''用户登出模块
'''
@app.route('/user/logout/')
def logout():
    session.clear()
    return render_template('user/login.html')


'''添加用户模块
'''
@app.route('/user/create/', methods=['POST', 'GET'])
def created():
    if request.method == 'GET':
        return render_template('user/user_add.html')
    else:
        # 获取前端通过POST传进来的数据，通过列表生成式处理成字典
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        # 验证用户名是否存在
        if user.ValidateUser(data['username']):
            return render_template('user/user_add.html', error=u'用户名已存在')
        # 判断密码为空则提示错误
        if data['password'] == '':
            return render_template('user/user_add.html', error=u'密码不能为空')
        # 生成sql里需要的参数
        args = (data['username'],data['password'],data['sex'],data['age'],data['phone'],data['email'],data['role'])
        # 执行添加用户动作
        if user.UserAdd(args):
            return redirect('/user/list/')
        else:
            return render_template('user/user_add.html', error=u'用户添加失败')


'''更新用户模块
'''
@app.route('/user/update/', methods=['POST', 'GET'])
def update():
    # 查询出数据，post和get方法共用
    params = request.args if request.method == 'GET' else request.form
    uid = params.get('uid', '')
    sql = 'select * from user where id= %s' % uid
    rt_user = user.GetUser(sql)[0]

    # 判断请求规则
    if request.method == 'GET':
        return render_template('user/user_modify.html', user=rt_user)
    else:
        # 获取前端通过POST传进来的数据，通过列表生成式处理成字典
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        # 判断密码为空则提示错误
        if data['password'] == '':
            return render_template('user/user_modify.html', user=rt_user, error=u'密码不能为空')
        # 生成sql里需要的参数
        args = (data['password'],data['sex'],data['age'],data['phone'],data['email'],data['role'],data['uid'])
        # 执行更新动作
        if user.UserUpdate(args):
            return redirect('/user/list/')
        else:
            return render_template('user/user_modify.html', user=rt_user, error=u'更新失败')

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

