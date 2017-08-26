#!/usr/bin/python
#coding:utf-8

from flask import Flask,render_template,request
import util
app=Flask(__name__)


#注册页面
@app.route('/login',methods=['GET','POST'])
def sigin():
    if  request.method == 'GET':
		return render_template('login.html')
    elif  request.method == 'POST':
        info = ['username','passwd','sex','age','phone','email','role']
        Temp= []
        for n in info:
            Temp.append(request.form.get(n))
        m = zhuce(Temp[0],Temp[1],Temp[2],Temp[3],Temp[4],Temp[5],Temp[6])
        if msg == "exists":
            msg = "usesrname is exist"
            return render_template('login.html',msg = msg )
        else:
            return render_template('sigin.html',msg = msg )

#登陆页面入口
@app.route('/',methods=['GET','POST'])
def sigin():
    if request.method == 'GET':
		return  render_template('sigin.html')
    else request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        Values = login(username,passwd)
        if Values == 1 :
            l = "用户名或密码不正确"
            return  render_template('denglu.html',l = l) 
        elif Values== 2:
            m = "用户不存在"         
            return  render_template('denglu.html',m = m)
        else:
            return  render_template('log.html',Values=Values)

#删除用户
@app.route('/deleteuser')
def del_user():
    id = request.args.get('id')
    resault = delete_user(id)
    User =  select_user()
    return  render_template('log.html',User=User)
      
#查询
@app.route('/chaxun')
def chaxun():
    id = request.args.get('id')
    n = select_id(id)
    return render_template('chaxun.html',n=n)

#更新
@app.route('/update',methods=['GET','POST'])
def update():
   User_list = ['username','passwd','sex','age','phone','email','role','id']
    Temp = []
    for i in User_list:
        i.append(request.form.get(i))
    update(Temp[0],Temp[1],Temp[2],Temp[3],Temp[4],Temp[5],Temp[6],Temp[7])
    User =  select_user()
    return  render_template('log.html',User=User)

    


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
