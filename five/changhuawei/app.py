#!/usr/bin/env python
#coding:utf-8

from flask import Flask,request,render_template,redirect
from util import _reg,_login,chaxunall,chaxunone,_xiugai,_delete

app = Flask(__name__)
# 首页
@app.route('/')
@app.route('/index')
def index():
    return render_template("index01.html")
# 注册
@app.route('/reg/', methods=['GET', 'POST'])
def reg(): 
    if request.method == 'POST':
        # 获取用户输入
        username = request.form.get('name')
        passwd = request.form.get('passwd')
        sex = request.form.get('sex')
        phone = request.form.get('phone')
        email = request.form.get('email')
        role = request.form.get('role')
        age = request.form.get('age')
        #print username,passwd,sex,phone,email,role,age
    else:
        username = request.args.get('name')
        passwd = request.args.get('passwd')
        sex = request.args.get('sex')
        phone = request.args.get('phone')
        email = request.args.get('email')
        role = request.args.get('role')
        age = request.args.get('age')
        return render_template("zhuce.html")
    _reg(username,passwd,sex,age,phone,email,role)

    return redirect("/login/")
# 登录
@app.route('/login/', methods=['GET', 'POST'])
def login():
    res = {'code':0,'msg':''}
    if request.method == 'POST':
        # 获取用户输入
        username = request.form.get('name')
        passwd = request.form.get('passwd')
        # print username,passwd
    else:
        username = request.args.get('name')
        passwd = request.args.get('passwd')
        return render_template("login1.html", result = res)   
    ss = _login(username,passwd)
    if ss == None:
        res['code'] = 1
        res['msg'] = 'pass err'
        return render_template("login1.html", result = res)
    else:
        res['code'] = 0
        res['msg'] = 'ok'
        # print ss[0][-1]
        if ss[0][-1] == 0:
            return redirect("/xinxi/")
        return render_template("xinxi.html",result=ss)

# 人员信息页
@app.route('/xinxi/')
def xinxi():
    ss = chaxunall()
    #print ss
    return render_template("xinxi.html",result = ss)
# 修改
@app.route('/xiugai/', methods=['GET', 'POST'])
def xiugai():   
    if request.method == 'POST':
        # 获取用户输入
        username = request.form.get('name')
        passwd = request.form.get('passwd')
        sex = request.form.get('sex')
        phone = request.form.get('phone')
        email = request.form.get('email')
        role = request.form.get('role')
        age = request.form.get('age')
        print username,passwd,sex,phone,email,role,age,uid
    else:
        # username = request.args.get('name')
        # passwd = request.args.get('passwd')
        # sex = request.args.get('sex')
        # phone = request.args.get('phone')
        # email = request.args.get('email')
        # role = request.args.get('role')
        # age = request.args.get('age')
        uid = request.args.get('id')
        return render_template("xiugai.html")
    # print uid
        # return render_template("xiugai.html")
    uid = request.args.get('id')
    _xiugai(username,passwd,sex,age,phone,email,role,uid)

    # return redirect("/xinxi/")
# 删除
@app.route('/delete/',methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        # 获取用户输入
        uid = request.form.get('uid')
    else:
        uid = request.args.get('id') 
        # print uid
    res = _delete(uid)
    res = chaxunall()
    return render_template("xinxi.html",result=res)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True )



