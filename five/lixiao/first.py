#!/usr/bin/python
#coding:utf-8

from flask import Flask,request,render_template,redirect
import utils
import MySQLdb as mysql
con=mysql.connect(user='root',host='127.0.0.1',passwd='123456',db='reboot15',port=3306,charset='utf8')
con.autocommit(True)
cur = con.cursor()
app = Flask(__name__)


###首页###
@app.route('/')
def homepage():
    welcome = "welcome login system"
    return render_template('index.html',welcome=welcome)


###用户注册###
@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method=='GET':
        return render_template('reg.html')
    elif request.method=='POST':
        userlist = []
        #errmsg = ""
        #msgerr = ""
        #regsuc = ""
        id = request.form.get('id')
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        repasswd = request.form.get('repasswd')
        sex = request.form.get('sex')
        age = request.form.get('age')
        phone = request.form.get('phone')
        email = request.form.get('email')
        role = request.form.get('role')
        
        cur.execute('select * from user')
        res = cur.fetchall()
        for user in res:
            userlist.append(user[1])
            if username not in userlist:
                if len(passwd)>6 and passwd == repasswd:
                    cur.execute('insert into user (username,password,sex,age,phone,email,role) values ("%s","%s","%s","%s","%s","%s","%s")' %(username,passwd,sex,age,phone,email,role))
                    con.commit()
                    regsuc = 'user reg is success'
                    return render_template('login.html',regsuc=regsuc)
                else:
                    errmsg = 'passwd not is legal'
                    return render_template('reg.html',errmsg=errmsg)
            else:
                msgerr = 'user  already exist'
                return render_template('reg.html',msgerr=msgerr)

###用户登录###
@app.route('/login/',methods=['GET','POST'])
def login_user():
    errmsg = ""
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
   
        cur.execute('select * from user where username = "%s"' %username)
        res = cur.fetchall() 
        for user in res:
            if user[1] == username and user[2] == passwd:
                #return render_template('info.html',admin=res)
                if user[7] == "0":
                    return redirect('/admin/')
                else:
                    return render_template('info.html',admin=res)
            else:
                errmsg = "usernama or passwd is wrong"
                return render_template('login.html',errmsg=errmsg)
    return render_template('login.html')


###管理员登录
@app.route('/admin/',methods=['GET','POST'])
def admin():
    cur.execute('select * from user')
    res = cur.fetchall()
    return render_template('info.html',admin=res)


###删除用户
@app.route('/delete/',methods=['GET','POST'])
def delete():
    id = request.args.get('id')
    utils.dele(id)
    show_user = utils.search()
    return render_template('info.html',user=show_user)


###修改用户
#@app.route('/change/',methods=['GET','POST'])
#def change():
#    id = request.args.get('id')
#    user = utils.search_id()
#    return render_template('update.html',user=user)

@app.route('/update/',methods=['GET','POST'])
def update():
    if request.method == 'GET':
        id = request.args.get('id')
        cur.execute('select * from user where id = "%s"' %id)
        res = cur.fetchall()
        return render_template('update.html',user=res)
    elif request.method == 'POST':
        id = request.form.get('id')
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        sex = request.form.get('sex')
        age = request.form.get('age')
        phone = request.form.get('phone')
        email = request.form.get('email')
        role = request.form.get('role')
        cur.execute('update user set password="%s",sex="%s",age="%s",phone="%s",email="%s",role="%s" where id = %s'%(passwd,sex,age,phone,email,role,id))
        con.commit()
        cur.execute('select * from user where id = "%s"' %id)
        res = cur.fetchall()
        return render_template('info.html',admin=res)
            

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
