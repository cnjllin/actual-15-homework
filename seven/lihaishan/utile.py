#_*_coding:utf-8_*_
import pymysql as mysql
from flask import Flask,request,render_template,redirect


conn= mysql.connect(user="root",password="",db="lhs",charset="utf8",host="127.0.0.1")
conn.autocommit(True)
cur=conn.cursor()


def insert(table,file,data):
    sql="insert into %s (%s) values (%s)" %(table,",".join(file),",".join(["'%s'" % data[x] for x in file]))
    print sql
    try:
        res=cur.execute(sql)
        print sql
        if res:
           result={"code":1,"msg":"insert ok"}
    except Exception,e:
        result={"code":0,"errmsg":"repeat of user name "}
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


def list(table,file):
    sql="select * from %s" %table
    cur.execute(sql)
    res=cur.fetchall()
    print sql
    if res:
        user=({v:row[k]for k,v in enumerate(file)} for row in res)
        result={"code":1,"msg":user}
    else:
        result={"code":0,"errmsg":"data is null"}
    return result

def update(table,field,data):
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id=%s" %(table,','.join(conditions),data['id'])
    print sql
    res = cur.execute(sql)
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result


def delete(table,data):
    tag=False
    try:
        sql="delete  from %s where id='%s'" %(table,data)
        res=cur.execute(sql)
        conn.commit()
        tag=True
    except  Exception,e:
        print "Erro '%s'"%(sql)
    return  tag