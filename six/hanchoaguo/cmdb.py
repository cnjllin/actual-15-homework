#!/usr/bin/python
#coding:utf-8
from  util import zhuc,select,cha,cha1,shan,update
from flask import Flask,render_template,request,redirect

#注册页面入口
app=Flask(__name__)
@app.route('/login/',methods=['GET','POST'])
def sigin():
    if  request.method == 'GET':
         return render_template('login.html')
    elif  request.method == 'POST':
        users =  { k:v[0] for k,v in dict(request.form).items()}
        m = zhuc(users)
        return render_template('denglu.html',m=m )


#登陆页面入口
@app.route('/',methods=['GET','POST'])
def dengl():
    if request.method == 'GET':
        return  render_template('denglu.html')
    elif request.method == 'POST':
        users ={k:v[0] for k,v in  dict(request.form).items()}
        usera = select(users)
        if usera == "pr":
            a = "passwd error"
            return  render_template('denglu.html',a=a) 
        elif usera == "ur":
            b = "username is error"         
            return  render_template('denglu.html',b = b)
        else:
            return  redirect('/userlist/')

#用户列表
@app.route('/userlist/')
def userlist():
    b = ['id', 'username', 'passwd', 'sex', 'age', 'phone', 'email', 'role']
    date = cha()
    m = [dict((k,n[i])for i,k in enumerate(b))for n in date]
    return render_template('userlist.html',m=m)


#删除
@app.route('/shanchu/')
def delete():
    id = request.args.get('id')
    resault = shan(id)
    return redirect('/userlist/')
      
#修改
@app.route('/xiugai/')
def update1():
    users ={k:v[0] for k,v in  dict(request.args).items()}
    b = ['id','username','passwd','sex','age','phone','email','role']
    user = cha1(users['id'])
    res = {k:user[i] for i,k in enumerate(b)}
    return render_template('xiugai.html',res = res)

#更新
@app.route('/update/',methods=['GET','POST'])
def gengxin():
    a = {k:v[0] for k,v in dict(request.form).items()}
    id=a['id']
    update(a,id)
    return  redirect('/userlist/')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=400,debug=True)
