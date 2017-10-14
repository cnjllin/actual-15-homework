#! /usr/bin/env python
#_*_coding:utf-8_*_
import MySQLdb
import config
import util
import traceback

db=MySQLdb.connect(host=config.host,
                   user=config.user,
                   passwd=config.passwd,
                   db=config.db,
                   port=config.port,
                   charset=config.charset)
cur=db.cursor()
db.autocommit(True)

# table="user"
# field 是一个元组
# data 是一个字典

# 增
def insert(table,field,data):
     sql="insert into %s (%s) values(%s)"%(table,','.join(field),','.join(['"%s"'% data[x] for x in field]))
     try:    
         res=cur.execute(sql)
         util.WriteLog("sql","/tmp/info.log").info("insert:%s"%sql)
         result ={'code':0,'msg':'insert ok'}
     except:
         result={'code':1,'msg':'insert fail'}
         util.WriteLog("db","/tmp/error.log").error("Except:%s error:%s"%(sql,traceback.format_exc()))
     return result


# 删除
def delete(table,uid):
   sql="delete from %s where id =%s"%(table,uid)
   print sql
   try:
       util.WriteLog("sql","/tmp/info.log").info("delete:%s"%sql)
       cur.execute(sql)
       result ={'code':0,'msg':'ok'}
   except:
       result={'code':1,'msg':'delete fail'}
       util.WriteLog("db","/tmp/error.log").error("Except:%s error:%s"%(sql,traceback.format_exc()))
   return result

# 改
def update(table,field,data):
    conditions=['%s="%s"'%(k,data[k])for k in data]
    sql="update %s set %s where id=%s"%(table,','.join(conditions),data['id'])
    try:
        util.WriteLog("sql","/tmp/info.log").info("update:%s"%sql)
        cur.execute(sql)
        result={'code':0,'msg':'ok'}
    except:
        result={'code':1,'msg':'update fail'}
        util.WriteLog('db',"/tmp/error.log").error("Except:%s error:%s"%(sql,traceback.format_exc())) 
    return result

# 查所有用户
def list(table,field):
    sql="select * from %s"%table
    try:
        cur.execute(sql)
        res=cur.fetchall()
        util.WriteLog("sql","/tmp/info.log").info("getlist:%s"%sql)
        user=[{k:row[i] for i,k in enumerate(field)}for row in res]
        result={'code':0,'msg':user}
    except:
        result={'code':1,'msg':'data is null'}
        util.WriteLog('db',"/tmp/error.log").error("Except:%s error:%s"%(sql,traceback.format_exc())) 
    return result

# 查单用户
def get_one(table,field,data):
   if data.has_key("username"):
      sql='select * from %s where username="%s"'%(table,data['username'])
   else:
      sql='select * from %s where id="%s"'%(table,data['id'])
   try:
       cur.execute(sql)
       res=cur.fetchone()
       util.WriteLog("sql","/tmp/info.log").info("getone:%s"%sql)
       user={k:res[i] for i,k in enumerate(field)}
       result={'code':0,'msg':user}
   except:
       result={'code':1,'msg':'data is null'}
       util.WriteLog('db',"/tmp/error.log").error("Except:%s error:%s"%(sql,traceback.format_exc())) 
   return result

# 查字段
def select(table,data):
   sql='select %s from %s'%(data,table)
   try:
       cur.execute(sql)
       result=cur.fetchall()
       util.WriteLog("sql","/tmp/info.log").info("select:%s"%sql)
   except:
       util.WriteLog('db',"/tmp/info.log").error("Except:%s error:%s"%(sql,traceback.format_exc())) 
   return result
 

'''
# test

field=('username','password','role')
data=('lk','123456','1')
table="user"
a=insert(table,field,data)
print a


table="user"
uid=3
a=delete(table,uid)
print a

table="user"
field=['id','username','password','role']
a=list(table,field)
print a

table='user'
field=['id','username','password','role']
data={'id':'1','username':'xx','password':'xxxxxx','role':'1'}
a=update(table,field,data)
print a
'''
