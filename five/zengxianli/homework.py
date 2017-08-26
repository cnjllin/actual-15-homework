#! /bin/env python
#coding:utf-8
from flask import Flask,render_template,request
import MySQLdb as mysql

conn= mysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='reboot15',charset='utf8')
conn.autocommit(True)
cur=conn.cursor()





app=Flask(__name__)

    
    
                        
@app.route('/del/')#删除函数                    
def delid(): 
    id=request.args.get('id')
    sql="delete from user where id = %s" % id
    cur.execute(sql)
    sql="select * from user"
    cur.execute(sql) 
    res=cur.fetchall()                                  
    return render_template("index2.html",result=res)
    
    

        
#id号和用户名是唯一的，一旦注册无法更改        
@app.route('/update/',methods=["GET","POST"])#更新函数                    
def updid():
    if request.method=="GET":
        return render_template("update.html")
        
    if request.method=="POST":
        name=request.form.get('name').strip()#获取用户名
        password=request.form.get('password').strip()
        sex=request.form.get('sex').strip()
        age=request.form.get('age').strip()
        phone=request.form.get('phone').strip()
        sql="select * from user where username= %s" % name
        cur.execute(sql)
        res=cur.fetchall()
        num=0
        for data in res:
            num=num+1
        if (num==0):
            return "false" #更新时，判断输入的用户名如果未注册，无法更新该用户的信息
        else:
            if len(password) !=0:#前端提交的密码如果为空，保留原密码；如果不为空，则更新
                sql="update user set password ='%s' where username ='%s'" % (password,name)
                cur.execute(sql) 
            if len(sex) !=0:#前端提交的性别信息如果为空，保留原性别；如果不为空，则更新
                sql="update user set sex =%s where username ='%s'" % (sex,name)
                cur.execute(sql)  
            if len(age) !=0:#前端提交的年龄信息如果为空，保留原年龄；如果不为空，则更新
                sql="update user set age =%s where username ='%s'" % (age,name)
                cur.execute(sql)    
            if len(phone) !=0:#前端提交的电话信息如果为空，保留电话；如果不为空，则更新
                sql="update user set phone =%s where username ='%s'" % (phone,name)
                cur.execute(sql) 
        sql="select * from user"
        cur.execute(sql)
        res=cur.fetchall()
        return render_template("index2.html",result=res)
   
    


@app.route("/login/",methods=["GET","POST"])#登陆函数，登陆时只输入正确的用户名和密码即可登陆
def login():
    if request.method=="POST":
        
        name=request.form.get('LoginForm[email]').strip()
        password=request.form.get('LoginForm[password]').strip()
        sql="select * from user where username='%s' and password='%s'" % (name,password) 
        cur.execute(sql)
        res=cur.fetchall()
        num=0
        for data in res:
            num=num+1
        if (num ==0):
            return "登陆失败"
        else:
            
            sql="select * from user"
            cur.execute(sql)
            res=cur.fetchall()
            return render_template("index2.html",result=res) 
    if request.method=="GET":
        return render_template("index1.html")
          
            
            
#注册时用户名和id号必须是唯一的且不能为空，否则不能注册
@app.route("/reg/",methods=["GET","POST"])#注册（增加）函数,注册时只需提供用户名和密码即可，其它信息注册成功后再更新
def reg(): 
    if request.method=="POST":	
    	  id=request.form.get('id').strip()
    	  name=request.form.get('LoginForm[email]').strip()
          print name
    	  password=request.form.get('LoginForm[password]').strip()
    	  repass=request.form.get('LoginForm[checksum]').strip()
    	  sql="select username from user "
    	  cur.execute(sql)
    	  res=cur.fetchall()
    	  sql="select id from user "
    	  cur.execute(sql)
    	  res1=cur.fetchall()
    	  if len(name)==0 or len(id)==0:
    	      return "用户名或id号不能为空，请重新输入:"
    	  elif (name in res) or (id in res1):
              return "该用户名或id号已注册，请重新输入"
          else:
              if len(password)==0 or password !=repass:
                  return "密码输入有误"                
              else:
                  sql="insert into user values(%s,'%s','%s',0,0,0,0,0)" % (id,name,password) 

                  cur.execute(sql)        
                  return "恭喜你，注册成功"
                
    if request.method=="GET": 
        return render_template("reg1.html")	          
            
                


if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)	   
