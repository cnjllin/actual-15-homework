#!/usr/bin/python
#_*_ coding:utf-8 _*_

from flask import Flask,request,render_template,redirect
from daoru import insert,getone,list,updata,check
import pymysql as mysql
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

app = Flask(__name__)
#链接数据库
connect_db= mysql.connect(user="root",passwd="120450327",db="reboot15",charset="utf8",host="127.0.0.1")
connect_db.autocommit(True)
#创建游标
cur=connect_db.cursor()
filed=["id","username","passwd","phone","email","age","sex","role"]
#首页
@app.route("/index/")
def index():
    hello="Welcome to the canyon of the dead!"
    return render_template("index.html",hello=hello)

#用户界面
@app.route("/userlist/")
def  userlist():
    result=list("mylist",filed)
    if result["code"]==0:
        result = result["msg"]
    return  render_template("userlist.html",result=result)

#登录
@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        data={k:v[0] for k,v in dict(request.form).items()}
        result=getone("mylist",filed,data)
        if result['code']==0 and result['msg']['passwd']==data['passwd']:
            return redirect("/userlist/")
        else:
            result['errmsg']="user is exist ,passwd is wrong"
            return render_template("login.html",result=result['errmsg'])
    return render_template("login.html")


#增，注册
@app.route("/reg/",methods=["GET","POST"])
def registor():
    if request.method=="POST":
        filed=["username","passwd","phone","email","age","sex","role"]
        user={k:v[0] for k ,v in dict(request.form).items()}
        print user
        result=check("mylist",user)
        print result
        if result["code"]==1:
            return render_template("registor.html",c=result["err"])
        else:
            result_ = insert('mylist',filed,user)
            if result_["code"]==0:
               return  redirect("/login/")
            else:
              return  render_template("registor.html")
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
    if request.method=="POST":
        data=dict(request.form)
        data={k:v[0]for k,v in data.items()}
        result=updata("mylist",filed,data)
        if result["code"]==0:
            return  redirect("/userlist/")
        else:
            return render_template("update.html",result=result['errmsg'])
    else:
        uid=request.args.get("id","")
        data={"id":uid}
        result=getone("mylist",filed,data)
        if result["code"]==0:
            result=result["msg"]
        return render_template("update.html",result=result)

#查询界面

def check_(table,field):
    if request.method=="GET":
        uid=request.args.get("id","")
        data={"id":uid}
        result=getone("mylist",filed,data)
        if result["code"]==0:
            result=result["msg"]
        return render_template("check_.html",result=result)
    return render_template("userlist.html")

if __name__=='__main__':
     app.run(host='0.0.0.0',port=5000,debug=True)
