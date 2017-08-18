#!/usr/bin/python 
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template,redirect
import userinfo
test=Flask(__name__)

#注册页面
@test.route('/reg/')
def reg():
    return render_template('reg.html')

#注册表单
@test.route('/after-reg/',methods=['GET','POST'])
def afterreg():
    if request.method == 'GET':
        username=request.args.get('name')
        user_pass1=request.args.get('pwd')
        user_pass2=request.args.get('pwd1')
    elif request.method == 'POST':
        username=request.form.get('name')
        user_pass1=request.form.get('pwd')
        user_pass2=request.form.get('pwd1')
    print username,user_pass1,user_pass2
    if not userinfo.checkout_user_exist(username) and user_pass1 == user_pass2:
        f=open('user_message.db','a+')
        f.write("%s:%s \n" % (username,user_pass1))
        f.close()
        return render_template('reg.html',ok='Congratulations on your successful registration')
    else:
        return render_template('reg.html',ok='regist failed,agine')
#会员中心
@test.route('/userlist/')
def userlist():
    f = open('user_message.db', 'r')
    message=f.readlines()
    f.close()
    return render_template('userlist.html',msg=message)
#登陆页面
@test.route('/login/')
def login():
    return render_template('login.html')
#登陆表单
@test.route('/after-login/',methods=['GET','POST'])
def afterlogin():
    if request.method == 'GET':
        user_name=request.args.get('name')
        user_pass=request.args.get('pwd')
    elif request.method == 'POST':
        user_name=request.form.get('name')
        user_pass=request.form.get('pwd')
    print user_name,user_pass
    if userinfo.checkout_user_pass(user_name,user_pass):
        return redirect('/userlist/')
    else:
        return render_template('login.html',error='username or password is error')

if __name__ == '__main__':
    test.run(host='0.0.0.0',port=5678,debug=True)
