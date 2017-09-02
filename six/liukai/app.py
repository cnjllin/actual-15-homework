#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect
import utils

table="user"
field=['id','username','password','role']

app=Flask(__name__)

# 首页
@app.route('/')
@app.route('/index/')
def index():
    username=""
    return render_template("index.html",username=username)

#注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        user=utils.get_name(table,field,user_dict['username'])
        if  user:
           result={'code':1,'msg':'username is already'} 
           return render_template("reg.html",result=result)
        else:
           utils.insert(table,user_dict)
           result={'code':1,'msg':' register success'}
           return redirect("/login/")
    result={} 
    return render_template("reg.html",result=result)
      
# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        user=utils.get_name(table,field,user_dict['username'])
        if  user  and  user_dict['password'] in user :
           res=dict(zip(field,user))
           result=utils.list(table,field)
           return render_template("list.html",result=result,res=res)
        else:
           result={'code':1,'msg':'username or password  is error'}
           return render_template("login.html",result=result)
    result={}
    return render_template("login.html",result=result)

# 删除     (管理员，普通用户删除后跳到登录界面)
@app.route('/delete/',methods=['GET','POST'])
def delete():
    uid=request.args.get('id')
    print uid,table
    utils.delete(table,uid)
    #return render_template("list.html",result=result,res=res)
    return redirect("/login/")

# 更新界面
@app.route('/userinfo/',methods=['GET','POST'])
def userinfo():
     uid=request.args.get('id')
     result=utils.get_one(table,field,uid)
     print result
     return render_template("update.html",result=result)

# 刷新
@app.route('/update/',methods=['GET','POST'])
def update():
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       utils.update(table,field,user_dict)
       return  redirect("login")


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5555,debug=True)

