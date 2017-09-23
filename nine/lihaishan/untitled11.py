#_*_coding:utf-8_*_
import pymysql as mysql
from flask import Flask,request,render_template,redirect,session
from utile import insert,getone,list,update,delete,check
import json
import  config
import util

app = Flask(__name__)
app.secret_key="dsadfasfadsfasf"
conn= mysql.connect(config.host,config.user,config.password,config.db,charset="utf8")
#app.config.from_object(config)
conn.autocommit(True)
cur=conn.cursor()
filed=["id","username","passwd","phone","email","age","sex","role"]



#—————用户管理


#用户注册
@app.route('/reg/',methods=["GET","POST"])
def reg():
    if request.method=="POST":
        file=["username","passwd","phone","email","age","sex","role"]
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=insert("mylist",file,user)
        if result["code"]==0    :
            return  json.dumps(result)
        else:
            return  json.dumps(result)


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
                util.WriteLog("user").info("%s login succesful" %session["username"])
                #print(json.dumps(result))
                return json.dumps(result)
        else:
            result["errmsg"]="passwd is wrong"
            return json.dumps(result)
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
    if result["code"]==0:
        result = result["msg"]
        return  render_template("new-userlist.html",result=result)

#用户更新
@app.route("/listupdate/",methods=["GET","POST"])
def listupdate():
    if not session:
        return  redirect("/login")
    if request.method=="GET":
        uid=request.args.get("id","")
        data={"id":uid}
        result=getone("mylist",filed,data)
        if result["code"]==0:
            result=result["msg"]
        return  json.dumps(result)
        #return  render_template("new-userlist.html",result=result)

#个人信息编辑
@app.route('/userupdate/',methods=['GET','POST'])
def userupdate():
    if not session:
       return redirect('/login/')
    if request.method=='POST':
       data={k:v[0] for k,v in dict(request.form).items()}
       result=update("mylist",filed,data)
    return  json.dumps(result)

#修改密码
@app.route('/updata/pwd/',methods=['GET','POST'])
def updatapwd():
    if not session:
       return redirect('/login/')
    if request.method=='POST':
        data={k:v[0] for k,v in dict(request.form).items()}
        print data
        userdata={"id":data["id"],"passwd":data["npassword"]}
        #result=update("mylist",filed,userdata)
        result=check("mylist",filed,userdata)
        if result["code"]==0:
            data={"id":data["id"],"passwd":data["npassword"]}
            result=update("mylist",filed,data)
    return  json.dumps(result)

#删除
@app.route("/dlt/")
def dlt():
    if not session:
        return  redirect("/login/")
    data={k:v[0] for k,v in dict(request.args).items()}
    result=delete("mylist",data)
    return json.dumps(result)

#用户退出
@app.route("/logout/")
def logout():
    if session:
        session.clear()
    return  redirect("/login/")


#------------资产管理---机房管理
#机房管理界面
@app.route("/machinlist/")
def machinlist():
    if not session:
        return  redirect("/login/")
    filed=["id","username","address","phone"]
    result=list("machine",filed)
    if result["code"]==0:
        result = result["msg"]
    return  render_template("machine.html",result=result)


#添加机房
@app.route('/machinreg/',methods=["GET","POST"])
def machinreg():
    if request.method=="POST":
        file=["username","address","phone"]
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=insert("machine",file,user)
        print result
        if result["code"]==0    :
            return  json.dumps(result)
        else:
            return  json.dumps(result)


#机房更新
@app.route("/machinupdate/",methods=["GET","POST"])
def machinupdate():
    if not session:
        return  redirect("/login")
    filed=["username","address","phone"]
    if request.method=='POST':
        data={k:v[0] for k,v in dict(request.form).items()}
        result=update("machine",filed,data)
        return  json.dumps(result)
    else:
        uid=request.args.get("id","")
        data={"id":uid}
        result=getone("machine",filed,data)
        if result["code"]==0:
            result=result["msg"]
        #return  json.dumps(result)
        return  render_template("machinupdate.html",result=result)

#机房删除
@app.route("/machindlt/")
def machindlt():
    if not session:
        return  redirect("/login/")
    data={k:v[0] for k,v in dict(request.args).items()}
    result=delete("machine",data)
    return json.dumps(result)


#------------资产管理---机柜管理


#机柜管理界面
@app.route("/cbtenlist/")
def cbtenlist():
    if not session:
        return  redirect("/login/")
    filed=["id","username","address","U","power"]
    result=list("cbten",filed)
    if result["code"]==0:
        result = result["msg"]
    return  render_template("cbtenlist.html",result=result)

#用户更新
@app.route("/cbtenupdate/",methods=["GET","POST"])
def cbtenupdate():
    if not session:
        return  redirect("/login/")
    filed=["id","username","address","U","power"]
    if request.method=='POST':
        data={k:v[0] for k,v in dict(request.form).items()}
        result=update("cbten",filed,data)
        return  json.dumps(result)
    else:
        uid=request.args.get("id","")
        data={"id":uid}
        result=getone("cbten",filed,data)
        if result["code"]==0:
            result=result["msg"]
        #return  json.dumps(result)
        return  render_template("cbtenupdate.html",result=result)

#添加机柜
@app.route('/cbtenreg/',methods=["GET","POST"])
def cbtenreg():
    if request.method=="POST":
        file=["username","address","U","power"]
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=insert("cbten",file,user)
        print result
        if result["code"]==0    :
            return  json.dumps(result)
        else:
            return  json.dumps(result)

#机柜删除
@app.route("/cbtendlt/")
def cbtendlt():
    if not session:
        return  redirect("/login/")
    data={k:v[0] for k,v in dict(request.args).items()}
    result=delete("cbten",data)
    return json.dumps(result)


#------------资产管理---服务器管理
@app.route("/severlist/")
def severlist():
    if not session:
        return  redirect("/login/")
    fileds = ['id','hostname', 'ip', 'mac', 'username', 'password', 'port', 'idc', 'brand', 'cpu', 'memory', 'disk', 'system_type', 'number']
    result=list("server",fileds)
    if result["code"]==0:
        result = result["msg"]
    return  render_template("severlist.html",result=result)



#添加服务器
@app.route('/addsever/',methods=["GET","POST"])
def addsever():
    if request.method=="POST":
        fileds = ['hostname', 'ip', 'mac', 'username', 'password', 'port', 'idc', 'brand', 'cpu', 'memory', 'disk', 'system_type', 'number']
        user=  {k:v[0]for k,v in dict(request.form).items()}
        result=insert("server",fileds,user)
        print result
        if result["code"]==0    :
            return  json.dumps(result)
        else:
            return  json.dumps(result)


#------------工单系统--工单申请
#机房管理界面
@app.route("/jobadd/",methods=["GET","POST"])
def jobadd():
    if not session:
        return  redirect("/login/")
    if request.method=="GET":
        return  render_template("jobapplication.html")
    if request.method=="POST":
        job= {k:v[0] for k,v in dict(request.form).items()}
        job['apply_name'] = session['username']
        file = ['apply_name',"apply_type",'apply_desc']
        result=insert("job",file,job)
        if result["code"]==0:
            return json.dumps(result)

#工单列表界面
@app.route("/joblist/")
def joblist():
    if not session:
        return  redirect("/login/")
    file = ['id','apply_name','handle_name','apply_type','apply_desc','handle_desc','status','created','modified']
    result=list("job",file)
    if result["code"]==0:
        result = result["msg"]
    return  render_template("joblist.html",result=result)


#工单更新
@app.route("/jobupdate/",methods=["GET","POST"])
def jobupdate():
    if not session:
        return  redirect("/login")
    if request.method=='POST':
        file=["id",'handle_desc','status']
        job={k:v[0] for k,v in dict(request.form).items()}
        job['status'] = 2
        result=update("job",file,job)
        if result["code"]==0:
            return  json.dumps(result)
    else:
        fiel = ['id','handle_name','status']
        job  = {k:v[0] for k,v in dict(request.args).items()}
        job['handle_name'] =  session['username']
        job['status'] = 1
        result =update('job',fiel,job)
        if  result['code'] == 0:
            result ={'code':0, 'msg':"Job Update  success"}
            return  json.dumps(result)

#详情
@app.route("/jobdetail/")
def jobdetail():
    if not session:
        return  redirect("/login/")
    job  = {k:v[0] for k,v in dict(request.args).items()}
    file = ['id','apply_name','created','apply_desc','apply_desc','handle_desc']
    result=getone("job",file,job)
    print result
    if result["code"]==0:
        result=result["msg"]
    #return  json.dumps(result)
    return render_template("user.html",result=result)



if __name__=='__main__':
     app.run(host='0.0.0.0',port=5000,debug=True)

