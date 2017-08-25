#!/usr/bin/python
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template,redirect
import userinfo
import MySQLdb as mysql
test=Flask(__name__)

#注册表单
@test.route('/reg/',methods=['GET','POST'])
def afterreg():
    if request.method == 'POST':
        username=request.form.get('name')
        user_pass1=request.form.get('pwd')
        user_pass2=request.form.get('pwd1')
        if not userinfo.checkout_user_exist(username) and user_pass1 == user_pass2:
            db=mysql.connect(host='localhost',user='root',passwd='',port=3306,db='51reboot',charset='utf8')
            cur=db.cursor()
            sql="insert into user(u_name,password,sex,age,phone,email,role) values('%s','%s',1,31,1591113981,'288987@163.com',2)" % (username,user_pass1)
            cur.execute(sql)
            db.commit()
            return render_template('reg.html',ok='Congratulations on your successful registration')
        else:
            return render_template('reg.html',ok='regist failed,agine')
    else:
        username=request.form.get('name')
        user_pass1=request.form.get('pwd')
        user_pass2=request.form.get('pwd1')
        return render_template('reg.html')
#会员中心
@test.route('/userlist/')
def userlist():
    db = mysql.connect(host='localhost', user='root', passwd='', port=3306, db='51reboot', charset='utf8')
    cur = db.cursor()
    filed=['id','u_name','password','sex','age','phone','email','role']
    sql='select %s  from user' %  (','.join(filed))
    cur.execute(sql)
    s=cur.fetchall()
#    users=[dict((k,row[i]) for i,k in enumerate(filed)) for row in s]
    users=[[row[i] for i,k in enumerate(filed)] for row in s]
    return render_template('userlist.html',msg=users)

@test.route('/userlist/delete/',methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        user_id=request.form.get('id')
    else:
        user_id=request.args.get('id')
    db = mysql.connect(host='localhost', user='root', passwd='', port=3306, db='51reboot', charset='utf8')
    cur = db.cursor()
    print user_id
    sql="delete  from user where id='%s'" %  (user_id)
    cur.execute(sql)
    db.commit()
    return redirect('/userlist/')

@test.route('/userlist/update/',methods=['GET','POST'])
def update():    
    if request.method == 'POST':
        user_name=request.form.get('name')
        user_pass=request.form.get('pwd')
        user_newpass=request.form.get('new_pwd')
        db=mysql.connect(host='localhost', user='root', passwd='', port=3306, db='51reboot', charset='utf8')
        cur=db.cursor()
        print user_name ,user_pass
        sql="select * from user where u_name='%s' and password='%s'" %  (user_name,user_pass)
        print sql
        sql1="update user set password='%s' where u_name='%s'" % (user_newpass,user_name)
        print sql1
        print cur.execute(sql)
        if cur.execute(sql):
            cur.execute(sql1)
            db.commit()
            return render_template('update.html',error='Congratulations on your successful update')
        else:
            return render_template('update.html',error='update failed,agine')

    else:
        return render_template('update.html')

#登陆表单
@test.route('/login/',methods=['GET','POST'])
def afterlogin():
    if  request.method == 'POST':
        user_name=request.form.get('name')
        user_pass=request.form.get('pwd')
        if userinfo.checkout_user_pass(user_name,user_pass):
            return redirect('/userlist/')
        else:
            return render_template('login.html',error='username or password is error')
    else:
        return render_template('login.html')

#首页
@test.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    test.run(host='0.0.0.0',port=5678,debug=True)
