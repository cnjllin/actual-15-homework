#!/usr/bin/python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template,redirect
import pymysql as mysql
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

app = Flask(__name__)
#链接数据库
connect_db= mysql.connect(user="root",passwd="",db="lhs",charset="utf8",host="127.0.0.1")
connect_db.autocommit(True)
#创建游标
cur=connect_db.cursor()

#首页
@app.route("/index/")
def index():
    hello="Welcome to the canyon of the dead!"
    return render_template("index.html",hello=hello)

#用户界面
@app.route("/userlist/")
def  userlist():
     sql="select * from mylist"
     cur.execute(sql)
     res=cur.fetchall()
     return  render_template("userlist.html",use=res)

#登录
@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = (request.form.get("username"))
        passwd = request.form.get("passwd")
        sql="select *from mylist where username='%s' and passwd=%s"%(username,passwd)
        if cur.execute(sql):
            return redirect("/userlist/")
        else:
            error=u"用户名错误或者密码错误"
            #print sql
            return render_template("login.html",ret=error)
    return render_template("login.html")

#增，注册
@app.route("/reg/",methods=["GET","POST"])
def registor():
    if request.method=="POST":
        username = request.form.get("username")
        passwd = request.form.get('passwd')
        repasswd = request.form.get('repasswd')
        sex = request.form.get('sex')
        phone = request.form.get('phone')
        email = request.form.get('email')
        age = int(request.form.get('age'))
        role=int(request.form.get("role"))
        if passwd==repasswd:
            sql="insert mylist (username,passwd,phone,email,age,sex,role) values ('%s',%s,%s,'%s',%d,%s,%d)"%(username,passwd,phone,email,age,sex,role)
            try:
                cur.execute(sql)
                return redirect("/login/")
            except Exception,e:
                error="%s already exists"%(username)
                #print cur.rowcount
                #print sql
                return render_template("registor.html",error=error)
        else:
            error=u"The two password input is inconsistent"
            return render_template("registor.html",cw=error)
    return render_template("registor.html")

#删除
@app.route("/dlt/",methods=["GET","POST"])
def delete():
    if request.method=="GET":
        useuid=int(request.args.get("id"))
        sql="delete from mylist where id=%d;" %(useuid)
        if cur.execute(sql):
            return redirect("/userlist/")
    return render_template("userlist.html")

#更新
@app.route("/update/",methods=["GET","POST"])
def update():
    if request.method=="GET":
        uid=int(request.args.get("id"))
        return render_template("update.html",uid=uid)
    if request.method=="POST":
        uid=request.form.get("id")
        nname=request.form.get("nname")
        npasswd=request.form.get("npasswd")
        nage=request.form.get("nage")
        nphone=request.form.get("nphone")
        sql="update mylist  set username='%s',passwd=%s,age=%s,phone=%s where id=%s" %(nname,npasswd,nage,nphone,uid)
        if cur.execute(sql):
            success=u"修改成功"
            return render_template("login.html",cg=success)
            #return redirect("/userlist/")
        else:
            fail=u"修改有误"
            return render_template("update.html",sb=fail)

#查询界面
@app.route("/check/",methods=["GET","POST"])
def check():
    if request.method=="GET":
        uid=request.args.get("id")
        sql="select * from mylist where id=%s" %(uid)
        cur.execute(sql)
        res=cur.fetchone()
        return render_template("check.html",result=res)
    return render_template("userlist.html")

if __name__=='__main__':
     app.run(host='0.0.0.0',port=5000,debug=True)
