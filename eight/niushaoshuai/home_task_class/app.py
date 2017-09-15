#!/usr/bin/python
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template,redirect,session
import utils
import json
test=Flask(__name__)
test.secret_key='sdfsfklsdlflfd'

filed=['id','username','password','role','email','phone','name']
update_filed=['id','username','name','email','phone']
insert_filed=['username','password','role','email','phone','name']

# 注册表单
@test.route('/add/',methods=['GET','POST'])
def add():
    if not session:
        return redirect("/login")
    if session['role']==0:
        if request.method == 'POST':
            user_info_dict=dict(request.form)
            user_data={ k:v[0] for k,v in user_info_dict.items() }
            if not utils.checkout_user_exist(user_data['name']) :
                res=utils.insert('user',insert_filed,user_data)
                return json.dumps(res)
        else:
            return render_template('add.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])
    else:    
        return render_template('index.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])
# 会员中心-首页
@test.route('/userlist/')
def userlist():
    if not session:
        return redirect("/login")
    if session['role']==0:
        users=utils.list('user',filed)
        users1=json.dumps({'code':0,'users':users})
        if users['code'] == 0:
            return render_template('userlist.html',msg=users['msg'],user=session['username'],role=session['role'])
#            return json.dumps({'code':0,'users':users})
    else:
        return render_template('userlist.html',user=session['username'],role=session['role'])
# 个人用户-首页
@test.route('/userlist1/')
def userlist1():
    if not session:
        return redirect("/login")
    else:
        user_id=session['id']
        users=utils.getone('user',filed,user_id)
#        users1=json.dumps({'code':0,'users':users})
        if users['code'] == 0:
            return render_template('userlist.html',msg=users['msg'],user=users)

# 会员中心-删除模块
@test.route('/delete/',methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        user_id=request.form.get('id')
    else:
        user_id=request.args.get('id')
    utils.delete('user',user_id)
    return redirect('/userlist/')

# 会员中心-更新模块
@test.route('/update',methods=['GET','POST'])
def update():    
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user=utils.update('user',user_data) 
        users=json.dumps(user)
        return json.dumps(user)

    else:
        user_id=request.args.get('id')
        data=dict()
        data['id']=user_id
        user=utils.getone('user',filed,data)
        if user['code'] == 0:
            return json.dumps(user['msg'])

# 会员中心-更新密码
@test.route('/user/chpwdoneself',methods=['GET','POST'])
def update_chpwdone():
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user=utils.update_passwd('user',session['id'],user_info_dict)
        users=json.dumps(user)
        return users
# 登陆模块
@test.route('/login/',methods=['GET','POST'])
def afterlogin():
    if  request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user_all=utils.getone('user',filed,user_data) 
        if user_all['code'] == 0 and utils.checkout_user_pass(user_data['username'],user_data['password']):
            session['id']=user_all['msg']['id']
            session['username']=user_all['msg']['username']
            session['name']=user_all['msg']['name']
            session['email']=user_all['msg']['email']
            session['phone']=user_all['msg']['phone']
            session['role']=user_all['msg']['role']
            return redirect('/')
        else:
            return render_template('login.html',error='username or password is error')
        
    return render_template('login.html')


# 登出
@test.route('/logout/')
def logout():
    session.clear()
    return redirect("/login")


# 首页
@test.route('/')
def index():
    if not session:
        return redirect("/login")
    else:
        return render_template('index.html',id=session['id'],user=session['username'],user_cn=session['name'],email=session['email'],phone=session['phone'],role=session['role'])

# 测试母版
@test.route('/base/')
def base():
    return render_template("base.html")

if __name__ == '__main__':
    test.run(host='0.0.0.0',port=5678,debug=True)
