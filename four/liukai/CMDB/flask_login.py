#!/usr/bin/env python
# *_coding:utf-8_*_
from flask import Flask,render_template,request,redirect
import user_login

app=Flask(__name__)

# 登录主界面
@app.route("/")
def login():
    return render_template('login.html')

# admin管理界面
@app.route("/login/",methods=["GET","POST"])
def manager():
   user=request.form.get('user')
   pwd=request.form.get('pwd')
   print user,pwd
   h=user_login.login(user,pwd)
   print h
   if h=='1':
       error='user or password is error '
       return render_template('error.html',error=error)
   elif h=='0':
       doct=user_login.read_file()
       print doct
       return render_template('user_show.html',doct=doct)
   else:
       doct=user_login.read_file()
       list=doct[user]
       print user,list
       return render_template('user.html',list=list,user=user) 

# 注册界面
@app.route("/zhuce/")
def zhuce():
   return render_template('zhuce.html')

# 注册信息写入文件，返回成功信息   
@app.route("/tianjia/",methods=["GET","POST"])
def tianjia():
   user=request.form.get('user')
   pwd=request.form.get('pwd')
   mail=request.form.get('mail')
   phone=request.form.get('phone')
   num=user_login.register(user,pwd)
   print num
   if num=="1":
       error="username is  already use or password < 6"
       return render_template('error.html',error=error)
   else:
       new_user_dict={}
       new_user_list=[]
       new_user_list.append(pwd)
       new_user_list.append(mail)
       new_user_list.append(phone)
       new_user_dict[user]=new_user_list
       user_login.write_file(new_user_dict)
       return render_template('user.html',list=new_user_list,user=user)


if __name__=="__main__":
   app.run(host='0.0.0.0',port=5000,debug=True)
