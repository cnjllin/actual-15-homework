#!/usr/bin/python 
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template
test=Flask(__name__)

@test.route('/reg/')
def reg():
    username=request.args.get('name')
    userpass=request.args.get('passwd')
    f = open('user_message.db', 'a+')
    f.write("%s:%s \n" % (username,userpass))
    return "reg ok,welcom %s .your pass is %s" % (username,userpass)

@test.route('/login/')
def login():
    username=request.args.get('name')
    userpass=request.args.get('passwd')
    print dict(request.args)
    return "login ok,welcom %s" % (username)

@test.route('/index/',methods=['GET','POST'])
def index():
    username=request.args.get('name')
    userpass=request.args.get('passwd')
    my_methods=request.method
    return "access methods is  %s" % (my_methods)

@test.route('/jinja/')
def jinja():
    str1='my first jinja'
    str2=["hello","world","huahua"]
    str=[{'name':'huahua','age':'18'},{'name':'huahua1','age':'118'}]
    str3=request.args.get('argss')
    username=request.args.get('name')
    userpass=request.args.get('pwd')
    f=open('user_message.db','a+')
    f.write("%s:%s\n" % (username,userpass))
#    return render_template('tongji.html',usermethod=str)
    return render_template('login.html')

if __name__ == '__main__':
    test.run(host='0.0.0.0',port=5678,debug=True)
