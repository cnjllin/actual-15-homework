#!/usr/bin/ env python 
#coding:utf-8

#实现注册的代码 
#在用户名和密码框中输入用户名密码,点击add提交按钮直接写入到users.txt文件中
 
from flask import Flask,render_template,redirect,request
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('form.html')
 
@app.route('/adduser')
def adduser():
    name = request.args.get('name','')
    pwd = request.args.get('password','')
    with open('users.txt','a+') as files:
        files.write('%s:%s\n' %(name,pwd))
    return redirect("/web4")
 
@app.route('/web4')
def web4():
       # tmp =  request.args.get('word','web3')
       # age =  request.args.get('age',14)
        #arr = [{'name':'one','age':14},{'name':'two','age':32},{'name':'three','age':9}]
        f = open('users.txt')
        arr = [ line.split(":")  for line in f.read().split('\n') ]
        print arr
       # return render_template('web3_2.html',word = tmp,age = age ,arr = arr)
        return render_template('web3_2.html',arr = arr)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
