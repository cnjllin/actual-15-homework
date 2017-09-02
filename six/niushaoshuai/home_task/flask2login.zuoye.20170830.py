#!/usr/bin/python
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template,redirect
import utils
test=Flask(__name__)

filed=['id','u_name','password','sex','age','phone','email','role']
insert_filed=['u_name','password','sex','age','phone','email','role']

# 注册表单
@test.route('/reg/',methods=['GET','POST'])
def afterreg():
    if request.method == 'POST':
        username=request.form.get('name')
        user_pass1=request.form.get('pwd')
        user_pass2=request.form.get('pwd1')
        user_sex=request.form.get('sex')
        user_age=request.form.get('age')
        user_phone=request.form.get('phone')
        user_email=request.form.get('email')
        user_role=request.form.get('role')
        if not utils.checkout_user_exist(username) and user_pass1 == user_pass2:
            utils.insert('user',insert_filed,username,user_pass1,user_sex,user_age,user_phone,user_email,user_role)
            return render_template('reg.html',ok='Congratulations on your successful registration')
        else:
            return render_template('reg.html',ok='regist failed,agine')
    else:
        return render_template('reg.html')

# 会员中心-首页
@test.route('/userlist/')
def userlist():
    users=utils.list('user',filed)
    return render_template('userlist.html',msg=users)

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
        user_id=request.form.get('id')
        user_name=request.form.get('name')
        user_pass=request.form.get('pwd')
        user_sex=request.form.get('sex')
        user_age=request.form.get('age')
        user_phone=request.form.get('phone')
        user_email=request.form.get('email')
        user_role=request.form.get('role')
        value=[user_id,user_name,user_pass,user_sex,user_age,user_phone,user_email,user_role]
        user=utils.update('user',filed,value,user_id) 
        return render_template('update.html',msg=user,error='update ok')

    else:
        user_id=request.args.get('id')
        user=utils.getone('user',filed,user_id)
        return render_template('update.html',msg=user)

# 登陆模块
@test.route('/login/',methods=['GET','POST'])
def afterlogin():
    if  request.method == 'POST':
        user_name=request.form.get('name')
        user_pass=request.form.get('pwd')
        print user_name
        user_id=utils.getid('user',user_name) 
        user_role=utils.getrole('user',user_name)
        if utils.checkout_user_pass(user_name,user_pass):
            if user_role == 0:
                return redirect('/userlist/')
            else:
                users=utils.getone('user',filed,user_id)    
                print users
                return render_template('userlist.html',msg=users)
        else:
            return render_template('login.html',error='username or password is error')
    else:
        
        return render_template('login.html')

# 首页
@test.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    test.run(host='0.0.0.0',port=5678,debug=True)
