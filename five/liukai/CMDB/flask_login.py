#!/usr/bin/env python
# *_coding:utf-8_*_
from flask import Flask,render_template,request,redirect,session
import utils

app=Flask(__name__)

# 主界面
@app.route("/",methods=['GET','POST'])
def login():
    res={'code':0,'msg':''}
    return render_template('login.html',res=res)

# 登录界面
@app.route("/login/",methods=["GET","POST"])
def manager():
   if request.method=="POST":
       username=request.form.get('user')
       password=request.form.get('pwd')
       print username,password
       d=utils.login(username,password)
       res={'code':0,'msg':''}
       print d
       if d=='1':
           res['code']=1
           res['msg']='user or password is error'
           return render_template('login.html',res=res)
       elif d=='0':
           return redirect("/admin/")
       else:
           admin="user"
           user_tup=utils.select_user(username)
           return render_template('user_show.html',admin=admin,user=user_tup)

# 管理员界面
@app.route("/admin/")
def admin():
      user_tup=utils.select_db()
      print user_tup
      admin="admin"
      return render_template('user_show.html',admin=admin,user=user_tup)



# 删除用户 
@app.route("/delete/",methods=['GET','POST'])
def delete():
      #if request.method=="POST":
          id=request.args.get('id')
          print id 
          utils.delete_db(id)
          user_tup=user_tup=utils.select_db()
          return render_template('user_show.html',user=user_tup)


# 修改用户信息
@app.route("/update/",methods=['GET','POST'])
def update():         
    id=request.args.get('id')
    user_tup=utils.select_id(id)
    #user_list=['password','sex','agr','phone','email','role']
    return render_template('update.html',user=user_tup)

# 
@app.route("/update_msg/",methods=['GET','POST'])
def update_msg():
    id=request.form.get('id')
    username=request.form.get('username')
    password=request.form.get('password')
    sex=request.form.get('sex')
    age=request.form.get('age')
    phone=request.form.get('phone')
    email=request.form.get('email')
    role=request.form.get('role')
    tup=(password,int(sex),int(age),int(phone),email,int(role),int(id))
    print tup
    p=utils.update_db(tup)
    #user_list=['password','sex','agr','phone','email','role']
    if p==0:
        user_tup=utils.select_user(username)
        return render_template('user_show.html',user=user_tup)


# 注册界面
@app.route("/zhuce/")
def zhuce():
   res={'code':0,'msg':''}
   return render_template('zhuce.html',res=res)


# 注册信息写入文件，返回成功信息   
@app.route("/register/",methods=["GET","POST"])
def register():
   username=request.form.get('user')
   password=request.form.get('pwd')
   sex=request.form.get('sex')
   age=request.form.get('age')
   phone=request.form.get('phone')
   email=request.form.get('email')
   num=utils.register(username,password)
   print num
   if num==1:
       res={'code':0,'msg':''}
       res['code']=1
       res['msg']="username is  already "
       return render_template('zhuc.html',res=res)
   elif num==2:
       res={'code':0,'msg':''}
       res['code']=1
       res['msg']="password < 6 "
       return render_template('zhuc.html',res=res)
   else:
       sex=int(sex)
       age=int(age)
       phone=int(phone)
       role=0
       a=utils.inster_db(username,password,sex,age,phone,email,role)
       if a==0:
            res={'code':0,'msg':''}
            res['msg']="reguster is ok "
            return render_template('login.html',res=res)

if __name__=="__main__":
   app.run(host='0.0.0.0',port=5000,debug=True)
