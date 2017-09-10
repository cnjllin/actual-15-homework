#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
import utils
import json
table="user"
field=['id','username','password','role']

app=Flask(__name__)
app.secret_key="sdafasdfasfd"

# 首页
@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        field=['username','password','role']
        user=utils.get_one(table,field,user_dict)
        print user 
        if user['code']==1:
            result=utils.insert(table,field,user_dict)
            #if result['code']==0:
            return json.dumps(result)
        else:
            result={'code':1,'msg':'username is error '}
            return json.dumps(result)
    #result={} 
    return render_template("reg.html")
      
# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        #uid=request.args.get('id')
        #user_dict={'id':uid}
        user=utils.get_one(table,field,user_dict)
        #return json.dumps(data)
        if  user['code']==0  and  user_dict['password']==user['msg']['password']:
           session['username']=user_dict['username']
           session['role']=user['msg']['role']
           data=user
           return json.dumps(data)
        
        else:
           data={'code':1,'msg':'username or password  is error'}
           return json.dumps(data)
    #result={}
    return render_template("login.html")

# 用户界面
@app.route('/user/')
def user():
    if not session:
        return redirect('/')
    username=session['username']
    user_dict={'username':username}
    result=utils.get_one(table,field,user_dict)
    #return json.dumps(data)
    return render_template('list.html',res=session ,result=result['msg'])


# 管理员用户列表
@app.route('/userlist/')
def userlist():
    if session:
        result=utils.list(table,field)
        print result['msg']
        print session
        if result['code']==0:
            return render_template('userlist.html',res=session,result=result['msg'])
        else:
            result={'code':1,'msg':'username or password  is error'}
            return render_template("login.html",result=result)
    else:
        return redirect("/login/")

# 管理员添加用户
@app.route('/add/',methods=['GET','POST'])
def add():
    if not session:
        return redirect('/')
    if request.method=='POST':
        user={k:v[0] for k,v in dict(request.form).items()}
        field=['username','password','role']
        if user['username'] and user['password']:
            data=utils.insert(table,field,user)
            return json.dumps(data)
        else:
           data={'code':1,'errmsg':'username or password is not null'}
           return json.dumps(data)
    return render_template("add.html")


# 删除   
@app.route('/delete/',methods=['GET','POST'])
def delete():
    if not session:
       return redirect('/')
    uid=request.args.get('id')
    print uid,table
    data=utils.delete(table,uid)
    #return render_template("list.html",result=result,res=res)
    #return redirect("/login/")
    return json.dumps(data)

# 修改界面
@app.route('/userinfo/',methods=['GET','POST'])
def userinfo():
     if not session:
         return redirect('/')
     if request.method=='GET':
         uid=request.args.get('id')
         data={'id':uid}
         result=utils.get_one(table,field,data)
         print "*******",result
         if result['code']==0:
            result=result['msg']
     return json.dumps(result)
      #   return render_template("update.html",result=result)

# 刷新
@app.route('/update/',methods=['GET','POST'])
def update():
    if not session:
       return redirect('/')
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       data=utils.update(table,field,user_dict)
       return  json.dumps(data)

# 用户登出
@app.route("/logout/")
def logout():
   if session:
      session.clear()
   return redirect("/")

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5555,debug=True)

