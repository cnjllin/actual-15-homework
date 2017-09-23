#_*_coding:utf-8_*_
import pymysql as mysql
from flask import Flask,request,render_template,redirect
import config
import util

conn= mysql.connect(config.host,config.user,config.password,config.db,charset="utf8")
conn.autocommit(True)
cur=conn.cursor()


def insert(table,file,data):
    sql="insert into %s (%s) values (%s)" %(table,",".join(file),",".join(["'%s'" % data[x] for x in file]))
    util.WriteLog("sql").info("insert:%s" % sql)
    res=cur.execute(sql)
    if res:
         result={"code":0,"msg":"insert ok"}
         print result
    else:
        result={"code":1,"errmsg":"repeat of user name "}
        print result
    return result

def getone(table,file,data):
    if data.has_key("username"):
        sql='select * from %s where username="%s"; ' %(table,data["username"])
    else:
        sql="select *from %s where id='%s'" %(table,data["id"])
    print sql
    cur.execute(sql)
    res=cur.fetchone()
    util.WriteLog("sql").info("getone:%s" % sql)
    if res:
        user={v:res[k] for k,v in enumerate(file)}
        result={"code":0,"msg":user}
    else:
        result={"code":1,"errmsg":"select fail"}
    return result


def check(table,file,data):
     sql="select *from %s where id='%s'" %(table,data["id"])
     util.WriteLog("sql").info("check:%s" % sql)
     cur.execute(sql)
     res=cur.fetchone()
     user={v:res[k] for k,v in enumerate(file)}
     print user["passwd"]
     passwd = request.form.get('passwd')
     print passwd
     if user["passwd"]==passwd:
         result={"code":0,"msg":"yes"}
     else:
        result={"code":1,"errmsg":"updata fail"}
     return result




def list(table,file):
    sql="select * from %s" %table
    util.WriteLog("sql").info("list:%s" % sql)
    cur.execute(sql)
    res=cur.fetchall()
    print sql
    if res:
        user=[{v:row[k]for k,v in enumerate(file)} for row in res]
        result={"code":0,"msg":user}
        print result
    else:
        result={"code":1,"errmsg":"data is null"}
    return result

def update(table,field,data):
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id=%s" %(table,','.join(conditions),data['id'])
    util.WriteLog("sql").info("update:%s" % sql)
    res = cur.execute(sql)
    if res :
        result = {'code':0,'msg':'update ok'}
        print result
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result


def delete(table,data):
    tag=False
    sql="delete  from %s where id='%s'" %(table,data["id"])
    util.WriteLog("sql").info("delete:%s" % sql)
    res=cur.execute(sql)
    conn.commit()
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result

