#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
db=mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')
cur = db.cursor()




#查询所有用户
def select_user():
    sql = "select * from user"
    res = cur.execute(sql)
    res=cur.fetchall()
    return res


#通过id查询 用户
def select_id(id):
    sql = "select * from user where id = %s"%id
    res = cur.execute(sql)
    res=cur.fetchone()
    return res


#update
def update(username,passwd,sex,age,phone,eamil,role,id):
     sql = "update user set username = '%s',password='%s',sex='%s',age='%s',phone='%s',email='%s',role='%s' where id =%s"%(username,passwd,sex,age,phone,eamil,role,id)
     res = cur.execute(sql)
     db.commit()


#注册用户
def zhuce(username,passwd,sex,age,phone,email,role):
     userlist = []
     res = select_user()
     for i in res:
         userlist.append(i[1])
     if username in userlist:
         return 'exists'
     else:       
         sql = "insert into user(username,password,sex,age,phone,email,role) values(%s,%s,%s,%s,%s,%s,%s)"
         res = cur.execute(sql,(username,passwd,sex,age,phone,email,role))
         db.commit()
  
         return  "登陆成功，欢迎回来"

#删除用户
def delete_user(id):
	sql = "delete from hanchaoguo where id = %s" %id
    res = cur.execute(sql)
    db.commit()
  


#登录
def login(username,passwd):
   users = []
   passwd_list = []
   res = select_user()
   for n in res:
       users.append(n[1])
       passwd_list.append(n[2])
   if username in users:
       if passwd == passwd_list[users.index(username)]:
           return res
       else:
           return 1
   else:
       return 2

#


