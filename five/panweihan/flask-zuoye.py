#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask, request, render_template,redirect
import MySQLdb as mysql
db = mysql.connect(host="127.0.0.1", user="root", passwd="123456", db="reboot15", port=3306, charset='utf8')
db.autocommit(True)
cur = db.cursor()

app = Flask(__name__)

# 用户首页
@app.route('/',methods=["GET","POST"])
@app.route('/index/',methods=["GET","POST"])
def index():
    return render_template("index.html")

# 登陆页面
@app.route('/login/',methods=["GET","POST"])
def login():   # 从数据库获取用户名和密码
    if request.method == "POST":
        name = request.form.get('username')
        pwd = request.form.get('password')
        sql = "select * from user where username = '%s'" % name
        cur.execute(sql)
        m = cur.fetchall()
        if m:
            if pwd == m[0][2]:
                return redirect('/home/')
            else:
                return render_template("login.html",error = "密码错误")
        else:
            return render_template("login.html",error = "用户名错误")
    return render_template("login.html")

# 注册页面
@app.route('/reg/', methods=["GET", "POST"])
def reg():
    if request.method == "POST":
        name = request.form.get('username', None)
        pwd = request.form.get('password', None)
        pwd2 = request.form.get('password2', None)
        sex = request.form.get('sex', None)
        age = request.form.get('age', None)
        phone = request.form.get('phone', None)
        email = request.form.get('email', None)
        role = request.form.get('role', None)
        sql = "select * from user where username = '%s'" % name
        cur.execute(sql)
        m = cur.fetchall()
        if m:
            return render_template("reg.html",error = "%s已被使用" %name)
        elif pwd != pwd2:
            return render_template("reg.html",error = "两次密码不一致")
        else:
            sql = "insert into user (username,password,sex,age,phone,email,role) values('%s','%s','%s','%s','%s','%s','%s')" %(name, pwd, sex,age,phone,email,role)
            print sql
            cur.execute(sql)
            return redirect("/home/")
    return render_template("reg.html")

# 用户信息页面，登陆成功后跳转到这里
@app.route('/home/')
def home():
    sql = "select * from user"
    cur.execute(sql)
    m = cur.fetchall()
    return render_template("home.html", data = m)


# 更新模块，木有做到想要的效果。。
@app.route('/change/',methods=["GET", "POST"])
def change():
    id = request.args.get('id')
    print id
    if request.method == "POST":
        name = request.form.get('username', None)
        pwd = request.form.get('password', None)
        sex = request.form.get('sex', None)
        age = request.form.get('age', None)
        phone = request.form.get('phone', None)
        email = request.form.get('email', None)
        role = request.form.get('role', None)
        sql = "update user set username = '%s',password = '%s',sex ='%s',age='%s',phone='%s',email='%s',role='%s' where id = '%s'" %(name, pwd, sex,age,phone,email,role,id)
        cur.execute(sql)
        m = cur.fetchall()
        return redirect("/home/")
    return render_template("change.html")

@app.route('/delete/')
def delete():
    id = request.args.get('id')
    sql = "delete from user where id = '%s'" % id
    cur.execute(sql)
    m = cur.fetchall()
    db.commit()
    sql = "select * from user"
    cur.execute(sql)
    m = cur.fetchall()
    return render_template("home.html", data = m)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
