#!/usr/bin/python
#coding:utf-8
"""用户注册：获取get表单提交的用户名和密码 写入到线下文件"""
from flask import Flask,request,render_template
app = Flask(__name__)
@app.route("/reg/")
def registor():
    username = request.args.get("username")
    passwd = request.args.get('passwd')
    repasswd = request.args.get('repasswd')
    print username ,passwd
    with open("C:\\Users\\HP\\PycharmProjects\\untitled5\\abc.txt","a+") as f:
        if username!="" and passwd!="" and passwd==repasswd:
            f.write("%s:%s\n" %(username,passwd))
            return "hello world! welcome %s,passwd is %s" %(username,passwd)
        else:
            return render_template("registor.html")
@app.route("/registor/")
@app.route("/")
def index():
    return render_template("registor.html")



"""用户登录：获取post提交的参数(用户名和密码)  判断用户名和密码是否已注册，已注册跳转到登录成功界面，未注册，返回登录界面"""
app = Flask(__name__)
@app.route("/login/",methods=["POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username")
        passwd = request.form.get("passwd")
        print username,passwd
        mss=open("C:\\Users\\xxx\\PycharmProjects\\untitled5\\abc.txt")
        content=mss.readlines()
        mss.close()
        #print content
        new_list=[]
        for use in content:
            name_=use.rstrip("\n").split(":")
            new_list.append((name_[0],name_[1]))
            #print new_list
        for t in new_list:
            #print t
            if t[0]==username and t[1]==passwd:
                return render_template("polo.html",t=t)
        else:
            return render_template("login.html")

@app.route("/index/")
def index():
    return render_template("login.html")
if __name__=='__main__':
     app.run(host='0.0.0.0',port=8888,debug=True)


