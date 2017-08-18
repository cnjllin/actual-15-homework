#!/usr/bin/python
#coding:utf-8
import top10
import denglu
import zhuce
from flask import Flask,render_template,request

#注册页面入口
app=Flask(__name__)
@app.route('/login/',methods=['GET','POST'])
def sigin():
    username = request.form.get('username')
    passwd = request.form.get('passwd')
    passwdagin= request.form.get('passwdagin')
    a = zhuce.zhuc(username,passwd,passwdagin)
    return a

#登陆页面入口
@app.route('/denglu/',methods=['GET','POST'])
def dengl():
      username = request.form.get('username')
      passwd = request.form.get('passwd')
      b = denglu.denglu(username,passwd)
      if b =="true":
         usera=top10.dict_1()
         
         return  render_template('top10.html',usera = usera)
      else:
          return b
    

#登陆页面入口路由
@app.route('/',methods=['GET','POST'])
def biaoge():
    return  render_template('denglu.html')

#注册页面入口路由
@app.route('/deng/',methods=['GET','POST'])
def biaoge1():
    return  render_template('login.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=400,debug=True)
