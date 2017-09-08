#_*_coding:utf-8_*_
import pymysql as mysql
from flask import Flask,request,render_template,redirect,session
from utile import insert,getone,list,update,delete
import json

app = Flask(__name__)
app.secret_key="dsadfasfadsfasf"
conn= mysql.connect(user="root",password="",db="lhs",charset="utf8",host="127.0.0.1")
conn.autocommit(True)
cur=conn.cursor()
filed=["id","username","passwd","phone","email","age","sex","role"]

#主主页
@app.route("/index/")
def index():
    if not session:
        return  redirect("/login/")
    username="wd"
    return  render_template("index.html",username=username)

#用户注册
@app.route('/reg/',methods=["GET","POST"])
def reg():
    if request.method=="POST":
        file=["username","passwd","phone","email","age","sex","role"]
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=insert("mylist",file,user)
        if result["code"]==1    :
            return  redirect("/login/")
        else:
            return  render_template("new-reg.html",result=result["errmsg"])
    return render_template("new-reg.html")

#用户登录
@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        data={k:v[0]for k,v in dict(request.form).items()}
        result=getone("mylist",filed,data)
        if result["code"]==0:
            if result["msg"]["passwd"]==data["passwd"]:
                session["username"]=data["username"]
                session["role"]=result["msg"]["role"]
                print session
                if session["role"]==0:
                    result=result["msg"]
                    return  render_template("index.html",result=result)
                else:
                    return  redirect("/userinfo/")
            else:
                result["errmsg"]="passwd is wrong"
                return render_template("login.html",result=result)
        else:
            result["errmsg"]="usdad"
            return render_template("login.html",result=result["errmsg"])
    return render_template("login.html")

#用户信息
@app.route("/userinfo/")
def userinfo():
    if not session:
        return  redirect("/login/")
    data={'username':session['username']}
    result=getone("mylist",filed,data)
    print result
    if result["code"]==0:
        result=result["msg"]
    #return  json.dumps(result)
    return render_template("user.html",result=result)

#用户界面
@app.route("/userlist/")
def  userlist():
    if not session or session["role"]!=0:
        return redirect("/login/")
    result=list("mylist",filed)
    if result["code"]==1:
        result = result["msg"]
    return  render_template("new-userlist.html",result=result,info=session)

#用户更新
@app.route("/update/",methods=["GET","POST"])
def updata():
    if not session:
        return  redirect("/login")
    if request.method=="POST":
        data=dict(request.form)
        data={k:v[0]for k,v in data.items()}
        result=update("mylist",filed,data)
        if result["code"]==0:
            return  redirect("/userlist/")
        else:
            return render_template("new-updata.html",result=result['errmsg'])
    else:
        uid=request.args.get("id","")
        data={"id":uid}
        result=getone("mylist",filed,data)
        if result["code"]==0:
            result=result["msg"]
        return  render_template("new-updata.html",result=result)


#删除
@app.route("/dlt/")
def dlt():
    if not session:
        return  redirect("/login/")
    data = dict((k,v[0]) for k,v in dict(request.args).items())
    if delete("mylist",data["id"]):
        return redirect("/userlist/")

#用户退出
@app.route("/logout/")
def logout():
    if session:
        session.clear()
    return  redirect("/login/")


if __name__=='__main__':
     app.run(host='0.0.0.0',port=5000,debug=True)
