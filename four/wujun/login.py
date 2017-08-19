#!/usr/bin/env python
#coding:utf-8

from flask import Flask,request,render_template
app = Flask(__name__)

#检查用户名密码是否正确
def check_name(user,pwd):
    name = []
    res = {}
    with open('user.txt') as f:
        for i in f:
            Temp = i.strip('\n')
            Tmp = Temp.split(':')
            res[Tmp[0]] = Tmp[1]


        if user not in res:
            Tmp = "用户不存在，请注册"
        elif pwd != res[user] :
           Tmp = '用户名或密码错误'
        else:
            Tmp = "欢迎回来"

    return Tmp


#定义首页/为Index.html
@app.route('/')
def index():
    return render_template('index.html')


#登录
@app.route('/index')
def login():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    return check_name(user,pwd)

#注册
@app.route('/reg')
def reg():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    re_pwd = request.args.get('re_pwd')
    # return 'user,pwd'

    if len(user) == 0:
        res = "请输入用户！"

    elif pwd != re_pwd or len(pwd) == 0:
        res = "密码不一致或者密码为空！请重新输入"
    else:
        with open('user.txt', 'a') as f:
            f.write('%s:%s\n' %(user,pwd))
        res = "用户%s,注册成功,请登录"%(user)
    return res





@app.route('/register')
def register():
  return render_template('register.html')


if __name__ == '__main__':
     app.run(host='0.0.0.0',port=8080,debug=True)
