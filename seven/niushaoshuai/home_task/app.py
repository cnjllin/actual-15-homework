#!/usr/bin/python
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template,redirect,session
import utils
import json
test=Flask(__name__)
test.secret_key='sdfsfklsdlflfd'

filed=['id','u_name','password','sex','age','phone','email','role']
insert_filed=['u_name','password','sex','age','phone','email','role']

# 注册表单
@test.route('/reg/',methods=['GET','POST'])
def afterreg():
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        if not utils.checkout_user_exist(user_data['u_name']) and user_data['password'] == user_data['password1']:
            res=utils.insert('user',insert_filed,user_data)
            if res['code'] == 0:
                return redirect("/login/")
        else:
            return render_template('reg.html',ok='regist failed,agine')
    else:
        return render_template('reg.html')

# 会员中心-首页
@test.route('/userlist/')
def userlist():
    if not session:
        return redirect("/login")
    else:
        users=utils.list('user',filed)
        users1=json.dumps({'code':0,'users':users})
        if users['code'] == 0:
            return render_template('userlist.html',msg=users['msg'])
#            return json.dumps({'code':0,'users':users})

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
@test.route('/update/',methods=['GET','POST'])
def update():    
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user=utils.update('user',filed,user_data) 
        if user['code']==0:
              return redirect("/userlist/")
        else:
             return render_template('update.html',error=user['msg'])

    else:
        user_id=request.args.get('id')
        user=utils.getone('user',filed,user_id)
        if user['code'] == 0:
            return render_template('update.html',msg=user['msg'])

# 登陆模块
@test.route('/login/',methods=['GET','POST'])
def afterlogin():
    if  request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user_id=utils.getid('user',user_data['u_name']) 
        user_role=utils.getrole('user',user_data['u_name'])
        if utils.checkout_user_pass(user_data['u_name'],user_data['password']):
            session['username']=user_data['u_name']
            session['id']=user_id
            session['role']=user_role
            if user_role == 0:
                return redirect('/userlist/')
            else:
                return redirect('/userlist1/')
        else:
            return render_template('login.html',error='username or password is error')
    else:
        
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
        return render_template('index.html')
if __name__ == '__main__':
    test.run(host='0.0.0.0',port=5678,debug=True)
