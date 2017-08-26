# -*- coding:utf-8 -*-
from app import app
from flask import g,session,render_template,request,url_for,redirect
from util import chaxun, insert,delete,select,update,cha_uid


@app.route('/',methods=['GET','POST'])
@app.route('/index/',methods=['GET','POST'])
def index():
    userinfos = chaxun()
    return render_template('index.html',users = userinfos)

@app.route('/dele/',methods=['GET','POST'])
def dele():
    uid = request.args.get('id')
    result = delete(uid)
    userinfos = chaxun()
    #return redirect('index.html',users = userinfos)
    return render_template('index.html',users = userinfos)

@app.route('/upd/',methods=['GET','POST'])
def upd():
    if request.method == 'GET':
        uid = request.args.get('id')
        userinfo = cha_uid(uid)
        return render_template('upd.html',n = userinfo)
    else :
        keys = ['uid','username','passwd','passwd1','age','sex','phone','email','role']
        users = {}
        for key in keys :
            users[key] = request.form.get(key)
        update(users)
        userinfos = chaxun()
        return render_template('index.html',users = userinfos)


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET' :
        return render_template('login.html')
    else :
        #passs
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        users = {}
        users['username'] = username
        users['passwd'] = passwd
        print users ,type(users)
        userinfo = select(users)
        print userinfo,type(userinfo)
        #return "xyz"
        if userinfo :
            if userinfo[2] == passwd :
                userinfos = chaxun()
                return render_template('index.html',users = userinfos)
            else :
                err_info = "passwd error"
                return  render_template('login.html',err_info = err_info) 
        else:
            #b = "用户名不存在"         
            err_info = "username not exisit"         
            return  render_template('login.html', err_info = err_info)

@app.route('/regist/',methods = ['GET','POST'])
def regist():
    if request.method == 'GET' :
        return render_template('regist.html')
    else :
        #passs
        keys = ['username','passwd','passwd1','age','sex','phone','email','role']
        users = {}
        for key in keys :
            users[key] = request.form.get(key)
        if users.get('passwd') == users.get('passwd1') :
            del users['passwd1']
            print users ,'123'
            if insert(users) :
                return redirect('/login/')
            else :
                err_info = "username already exists"
                return render_template('regist.html',m = err_info )
        else :
            m = "Two passwords are different"
            return render_template('regist.html',m = m )
        

@app.route('/logout/')
def logout() :
    #session.pop('user_id')
    #del session('user_id')
    session.clear()
    return redirect(url_for('login'))
