#! /bin/env python
#coding:utf-8
from flask import Flask,render_template,request
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

fo=open("user.txt")
users={}
content=fo.readlines()
fo.close()
for user in content:
    name=user.rstrip("\n").split(":")[0]
    users[name]=user.rstrip("\n").split(":")[1]


app=Flask(__name__)
@app.route('/login/')
@app.route('/reg/index1.html/')
@app.route('/login/index1.html/')
def login():
    return render_template("index1.html") #登陆界面  

@app.route('/reg/')
@app.route('/login/reg1.html/')
@app.route('/reg/reg1.html/')
def reg():
    return render_template("reg1.html")#注册界面


@app.route('/')
def zz():
    return render_template("index2.html")#登陆成功界面
    
    
    

       
    


@app.route("/login/",methods=["GET","POST"])#登陆判断函数
def logincheck():
    name=request.form.get('LoginForm[email]').strip()
    password=request.form.get('LoginForm[password]').strip()
    if name not in users:
        return "用户名不存在%s，无法登陆" % name
    else:
        if password !=users[name]:
            return "密码输入有误，无法登陆"
        else:
#            return "恭喜你，登陆成功"
            return render_template("index2.html",name=name)#跳转到登陆成功界面，把用户名从后端渲染到前端并显示出来
            
            
            

@app.route("/reg/",methods=["GET","POST"])#注册判断函数
def regcheck():
    name=request.form.get('LoginForm[email]').strip()
    password=request.form.get('LoginForm[password]').strip()
    repass=request.form.get('LoginForm[checksum]').strip()
    f=open('user.txt','a+')
    if len(name)==0:
        return "用户名不能为空，请重新输入:"
            
    elif name in users:
        return "该用户名已注册，请重新输入"
            
    else:
        
        
        if len(password)==0 or password !=repass:
#        	  return "%s,%s" % (password,repass)
            return "密码输入有误"
            
        else:
            f.write("%s:%s\n" % (name,password))
            f.close()
#            return "%s,%s no" % (password,repass)
            return "恭喜你，注册成功"
                






if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
