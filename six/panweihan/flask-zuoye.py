#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask, request, render_template, redirect
from utils import *

import MySQLdb as mysql
db = mysql.connect(host="127.0.0.1", user="root", passwd="123456", db="reboot15", port=3306, charset='utf8')
db.autocommit(True)
cur = db.cursor()

app = Flask(__name__)

# 首页
@app.route('/')
@app.route('/index/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


# 登陆页面
@app.route('/login/', methods=["GET", "POST"])
def login():  # 从数据库获取用户名和密码
    if request.method == "POST":
        data = dict((k,v[0]) for k, v in dict(request.form).items())
        sql = 'select * from old_user where username = "%s"' % data.get('username')
        cur.execute(sql)
        m = cur.fetchone()
        if m:
            if data.get('password') == m[2] and m[7] == "管理员":
                return redirect('/admin/')
            elif data.get('password') == m[2] and m[7] == "普通用户":
                return render_template("login.html",id = m[0])
            else:
                return render_template("login.html", error="密码错误")
        else:
            return render_template("login.html", error="用户名错误")
    return render_template("login.html")


# 注册页面
@app.route('/reg/', methods=["GET", "POST"])
def reg():
    if request.method == "POST":
        data = dict((k,v[0]) for k, v in dict(request.form).items())
        sql = "select * from old_user where username = '%s'" % data.get('username')
        cur.execute(sql)
        m = cur.fetchone()
        if m:
            return render_template("reg.html", error="%s已被使用" % data.get('username'))
        elif data.get('password') != data.get('password2'):
            return render_template("reg.html", error="两次密码不一致")
        else:
            del data['password2']
            fields,values = [],[]
            for k,v in data.items():
                fields.append(k)
                values.append("'%s'" %v)   # 注意，%s外面双引号套单引号
            sql = "insert into old_user (%s) values (%s)"  %(','.join(fields),','.join(values))
            print sql
            cur.execute(sql)
            return redirect("/login/")
    return render_template("reg.html")


# 用户信息页面，登陆成功后跳转到这里
@app.route('/user/')
def home():
    id = request.args.get('id')
    sql = "select * from old_user where id = %s" %id
    cur.execute(sql)
    m = cur.fetchone()
    return render_template("user.html", data=m)

# 管理员页面
@app.route('/admin/')
def admin():
    sql = "select * from old_user"
    cur.execute(sql)
    m = cur.fetchall()
    return render_template("admin.html", data=m)

# 更新模块
@app.route('/change/', methods=["GET", "POST"])
def change():
    id = request.args.get('id')  # 这个ID能取到值
    sql = "select * from old_user where id = '%s'" % id
    cur.execute(sql)
    m = cur.fetchone()
    if request.method == "POST":
        data = dict((k,v[0]) for k, v in dict(request.form).items())
        id = data['id']
        del data['id']
        conditions = ["%s='%s'"% (k,data[k]) for k in data]
        sql = 'update old_user set %s where id = %s' %(','.join(conditions), id)
        cur.execute(sql)
        return redirect("/admin/")
    return render_template("change.html", data=m)

# 删除用户
@app.route('/delete/')
def delete():
    id = request.args.get('id')
    sql = "delete from old_user where id = '%s'" % id
    cur.execute(sql)
    return redirect("/admin/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
