#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
db=mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')
db.autocommit(True)
cur = db.cursor()
#注册函数
def zhuc(users):
     sql = "insert into hanchaoguo (%s) values (%s);" %(','.join(users.keys()),','.join(users.values()))
     #sql = "insert into hanchaoguo(username,password,sex,age,phone,email,role) values(%s,%s,%s,%s,%s,%s,%s)"
     #res = cur.execute(sql,(users['username'],users['passwd'],users['sex'],users['age'],users['phone'],users['email'],users['role']))
     res = cur.execute(sql)
     return  "sescuss welcome"

#删除函数
def shan(id):
   sql = "delete from hanchaoguo where id = %s" %id
   res = cur.execute(sql)
  


#登录函数
def select(users):
   result = cha2(users['username'])
   if not result:  
       return  "ur"
   else:
        if users['passwd'] == result[2]:
           return cha()
        else:
           return "pr"

#查询所有函数
def cha():
    sql = "select * from hanchaoguo"
    res = cur.execute(sql)
    res=cur.fetchall()
    return res


#按id条件查找函数
def cha1(id):
    sql = "select * from hanchaoguo where id = %s"%id
    res = cur.execute(sql)
    res=cur.fetchone()
    return res


#按名字查
def cha2(username):
    sql = "select * from hanchaoguo where username = '%s'" %username
    res = cur.execute(sql)
    res=cur.fetchone()
    return res



#修改函数
def update(a,id):
     result=['%s = "%s"' %(k,a[k]) for k in a]
     sql = "update hanchaoguo set %s where id=%s" %(','.join(result),id) 
     res = cur.execute(sql)



