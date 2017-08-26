#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
db=mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')
cur = db.cursor()
#注册函数
def zhuc(username,passwd,sex,age,phone,email,role):
     userlist = []
     res = cha()
     for n in res:
         userlist.append(n[1])
     if username in userlist:
         return "error"
     else:       
         sql = "insert into user(username,password,sex,age,phone,email,role) values(%s,%s,%s,%s,%s,%s,%s)"
         res = cur.execute(sql,(username,passwd,sex,age,phone,email,role))
         db.commit()
  
         return  "sescuss welcome"

#删除函数
def shan(id):

   sql = "delete from user where id = %s" %id
   res = cur.execute(sql)
   db.commit()
  


#登录函数
def select(username,passwd):
   users = []
   passwd_list = []
   res = cha()
   for n in res:
       users.append(n[1])
       passwd_list.append(n[2])
   if username in users:
       if passwd == passwd_list[users.index(username)]:
           return res
       else:
           return "pr"
   else:
       return "ur"

#查询所有函数
def cha():
    sql = "select * from user"
    res = cur.execute(sql)
    res=cur.fetchall()
    return res


#按id条件查找函数
def cha1(id):
    sql = "select * from user where id = %s"%id
    res = cur.execute(sql)
    res=cur.fetchone()
    return res


#修改函数
def update(username,passwd,sex,age,phone,eamil,role,id):
     sql = "update user set username = '%s',password='%s',sex='%s',age='%s',phone='%s',email='%s',role='%s' where id =%s"%(username,passwd,sex,age,phone,eamil,role,id)
     res = cur.execute(sql)
     db.commit()



