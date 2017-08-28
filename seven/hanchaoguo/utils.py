#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
db=mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port
=3306,charset='utf8')
db.autocommit(True)
cur = db.cursor()




#增加
def insert(table,filed,users):
    sql = "insert into %s (%s) values (%s);" %(table,','.join(filed), ','.join([ '"%s"' %users[n] for n in filed]))
    print sql
    res = cur.execute(sql)
    if res:
        result ={'code':0,'msg':'insert is ok'}
    else:
        result ={'code':1,'msg':'insert is error'}
    return result

# 登录
def getone(table,filed,data):
    if data.has_key("username"):
        sql = 'select * from %s where username= "%s"' %(table,data['username'])
    else:
        sql = 'select * from %s where id = "%s"' %(table,data['id'])
    cur.execute(sql)
    res = cur.fetchone()
    if res:
      users = {k:res[i] for i,k in enumerate(filed)}
      user = {'code':0,'msg':users}
    else:
      user= {'code':1,'errmsg':'no users'}
    return user
    

#查询
def select(table,field):
    sql = "select * from %s" % table
    cur.execute(sql)
    res = cur.fetchall()
    if res:
       user = [{k:row[i] for i,k in enumerate(field)} for row in res]
       result = {'code':0,'msg':user}
    else:
       result = {'code':1,'msg':'data is null'}
    return result
# 更新
def update(table,filed,data):
    result=['%s = "%s"' %(k,data[k]) for k in filed]
    sql = "update %s set %s where id = %s" %(table,','.join(result),data['id'])
    print sql
    res = cur.execute(sql)
    if res:
         res = {'code':0,'msg':'update sucessfor'}
    else:
         res = {'code':1,'msg':'update failed'}
    return res
# 删除
def delete(table,filed,data):
    sql = "delete from %s where id = %s" %(table,data['id'])
    res=cur.execute(sql)
    if res:
        res = {'code':0,'msg':'delete secussfor'}
    else:
        res = {'code':1,'msg':'delete failed'}
    return res    





