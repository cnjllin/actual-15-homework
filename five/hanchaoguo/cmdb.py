#!/usr/bin/python
#coding:utf-8
from  util import zhuc,select,cha,cha1,shan,update
from flask import Flask,render_template,request

#注册页面入口
app=Flask(__name__)
@app.route('/login/',methods=['GET','POST'])
def sigin():
    if  request.method == 'GET':
         return render_template('login.html')
    elif  request.method == 'POST':
        info = ['username','passwd','sex','age','phone','email','role']
        a= []
        for n in info:
            a.append(request.form.get(n))
        m = zhuc(a[0],a[1],a[2],a[3],a[4],a[5],a[6])
        if m == "error":
            m = "usesrname is exist"
            return render_template('login.html',m = m )
        else:
            return render_template('denglu.html',m = m )

#登陆页面入口
@app.route('/',methods=['GET','POST'])
def dengl():
    if request.method == 'GET':
        return  render_template('denglu.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        usera = select(username,passwd)
        if usera == "pr":
            a = "passwd error"
            return  render_template('denglu.html',a = a) 
        elif usera == "ur":
            b = "username is error"         
            return  render_template('denglu.html',b = b)
        else:
            return  render_template('log.html',usera=usera)

#删除
@app.route('/shanchu/')
def delete():
    id = request.args.get('id')
    resault = shan(id)
    usera =  cha()
    return  render_template('log.html',usera=usera)
      
#修改
@app.route('/xiugai/')
def update1():
    id = request.args.get('id')
    n = cha1(id)
    return render_template('xiugai.html',n=n)

#更新
@app.route('/update/',methods=['GET','POST'])
def gengxin():
    info = ['username','passwd','sex','age','phone','email','role','id']
    a = []
    for n in info:
        a.append(request.form.get(n))
    update(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7])
    usera =  cha()
    return  render_template('log.html',usera=usera)

    


if __name__=='__main__':
    app.run(host='0.0.0.0',port=400,debug=True)
