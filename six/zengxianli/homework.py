#! /bin/env python
#coding:utf-8
from flask import Flask,render_template,request,redirect
import MySQLdb as mysql
import sys
reload(sys)
sys.setdefaultencoding('utf8')

conn= mysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='reboot15',charset='utf8')
conn.autocommit(True)
cur=conn.cursor()


app=Flask(__name__)


##检查用户名是否存在的函数，登陆和注册时都需调用
def checkusername(table,value):
    sql="select * from %s where username='%s'" % (table,value)
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        result={'code':0,'errmsg':'该用户未注册，无法登陆'}#注册时调用
        return result
    else:
        result={'code':1,'errmsg':'该用户已被注册，请重新输入'}#登陆时调用
        return result




##添加用户的函数，注册时调用
def insert (table,data):
    fields,values=[],[]
    for k,v in data.items():
        fields.append(k)
        values.append("'%s'" % v)
    sql="insert into %s (%s) value (%s)" % (table,','.join(fields),','.join(values))
    cur.execute(sql)
    result={'code':0,'errmsg':'ok'}
    return result

##删除用户的函数，删除时调用
def delete (table,uid):
    sql="delete from %s where id =%s" % (table,uid)
    cur.execute(sql)
    result={'code':0,'errmsg':'ok'}
    return result

##更新用户信息的函数，更新时调用
def updateid (table,fields):
    conditions=[]
    for k,v in fields.items():
        if k!='id' and v:
            conditions.append("%s='%s'" % (k,v)) 
    sql="update %s set %s where id =%s" % (table,','.join(conditions),fields['id'])
    cur.execute(sql)
    result={'code':0,'errmsg':'ok'}
    return result




##检查用户名和对应的密码是否正确的函数，登陆时调用
def checkuser(table,fields):
    conditions=[]
    for k,v in fields.items(): 
        conditions.append("%s='%s'" % (k,v))
    sql="select * from %s where %s" % (table,' AND '.join(conditions))
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        result={'code':1,'errmsg':'用户信息错误，请重新输入'}
        return result
    else:
        result={'code':0,'errmsg':'ok'}
        return result

##查看所有用户信息函数，用户列表页面时调用
def list(table):
    fields=['id','username','password','role']
    sql="select * from %s " % table
    cur.execute(sql)
    res=cur.fetchall()
    if not res:
        result={'code':1,'errmsg':'data is null'}
        return result
    else:
        user=[{k:row[i] for i,k in enumerate(fields)} for row in res]
        return user


##打开首页
@app.route("/")
@app.route("/index/")
def index():
    username="wd"
    return render_template("index.html",username=username)


##打开注册页面
@app.route("/reg/",methods=["GET","POST"])
def reg():
    user={} 
    result={}
    if request.method=="POST":
        user=dict ((k,v[0]) for k,v in dict(request.form).items())
        result=checkusername('user',user['username'])
        if result['code']==1:
            return render_template("reg1.html",result=result['errmsg'])
        elif not user['username']:
            return render_template("reg1.html",result="用户名为空，无法注册")
     	else: 
            insert('user',user)
            return  redirect('/login/')
    if request.method=="GET":
        return render_template("reg1.html")



##打开登陆页面
@app.route("/login/",methods=["GET","POST"])
def login():
    user={}
    result={}
    if request.method=="POST":
        user=dict ((k,v[0]) for k,v in dict(request.form).items())
        result=checkusername('user',user['username'])
        if result['code']==0:
            return render_template("login.html",result=result['errmsg'])
        elif not user['username']:
            return render_template("login.html",result="用户名为空，无法登陆")
        else:
            result=checkuser('user',user)
            if result['code']==1:
                return render_template("login.html",result=result['errmsg'])
            else:
                return  redirect('/userlist/')
    if request.method=="GET":
        return render_template("login.html")



##打开更新页面
@app.route("/update/",methods=["GET","POST"])
def update():
    if request.method=="POST":
        user=dict ((k,v[0]) for k,v in dict(request.form).items())
        updateid('user',user)
        return  redirect('/userlist/') 
    if request.method=="GET":
        uid=request.args.get('id')
        return render_template("update.html",id=uid)   



##展示用户列表页面
@app.route("/userlist/")
def userlist():
    uid=request.args.get('id')
    if uid:
        delete('user',uid)
    user=list('user')
    return render_template("userlist.html",result=user)


            
      

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)	        
