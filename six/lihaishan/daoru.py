#!/usr/bin/python
#_*_ coding:utf-8 _*_
import pymysql as mysql

connect_db= mysql.connect(user="root",passwd="120450327",db="reboot15",charset="utf8",host="127.0.0.1")
connect_db.autocommit(True)
#创建游标
cur=connect_db.cursor()

def insert(table,file,data):
    sql="insert into %s (%s) values(%s);" %(table,",".join(file), ",".join(["'%s'" %data[x] for x in file]))
    print sql
    res=cur.execute(sql)
    if res:
        result={"code":0,"msg":"insert ok"}
    else:
        result={"code":1,"errmsg":"insert fail"}
    return result


def list(table,field):
    sql="select *from %s" %table
    cur.execute(sql)
    res=cur.fetchall()
    if res:
        user=({v:row[k]   for k,v in enumerate(field)} for row in res)
        result={"code":0,"msg":user}
    else:
        result={"code":1,"errmsg":"data is null"}
    return result


def getone(table,file,data):
    if data.has_key("username"):
        sql='select * from %s where username="%s" ' %(table,data["username"])
    else:
        sql="select *from %s where id='%s'" %(table,data["id"])
    print sql
    cur.execute(sql)
    res=cur.fetchone()
    print res
    if res:
        user={v:res[k] for k,v in enumerate(file)}
        result={"code":0,"msg":user}
    else:
        result={"code":1,"errmsg":"updata fail"}
    return result


def updata(table,field,data):
    flag = False
    conditions={"%s='%s'" %(k,data[k])for k in data}
    sql="update %s set %s where id='%s'"%(table,",".join(conditions),data["id"])
    print sql
    print conditions
    res=cur.execute(sql)
    if res:
        result={"code":0,"msg":"updata ok"}
    else:
        result={"code":1,"errmsg":"updata fail"}
    return result


def check(table,data):
    sql='select * from %s where username="%s" ' %(table,data["username"])
    print sql
    cur.execute(sql)
    res=cur.fetchone()
    if res:
        result={"code":1,"erro":"user is exit"}
    else:
         result={"code":0,"erro":"user is exit"}
    return  result