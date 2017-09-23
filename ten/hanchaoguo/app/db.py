#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
import config
import utils
#db=mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port
#=3306,charset='utf8')
db=mysql.connect(host = config.db_host,
                 user = config.db_user,
                 passwd = config.db_passwd,
                 db = config.db_db,
                 port = config.db_port,
                 charset = 'utf8')
db.autocommit(True)
cur = db.cursor()



# 增
def insert(table,filed,data):
    sql = "insert into %s (%s) values (%s);" %(table,','.join(data), ','.join([ '"%s"' %data[n] for n in data]))
    utils.WriteLog(sql).info("insert %s:" %sql)
    res = cur.execute(sql)
    if res:
        result ={'code':0,'msg':'insert is ok'}
    else:
        result ={'code':1,'errmsg':'insert is error'}
    return result

# 查询单个用户
def getone(table,filed,data):
    if data.has_key("username"):
        sql = 'select * from %s where username= "%s"' %(table,data['username'])
    else:
        sql = 'select * from %s where id = "%s"' %(table,data['id'])
    utils.WriteLog(sql).info("getone %s:" %sql)
    cur.execute(sql)
    res = cur.fetchone()
    if res:
      users = {k:res[i] for i,k in enumerate(filed)}
      user = {'code':0,'msg':users}
    else:
      user= {'code':1,'errmsg':'no users'}
    return user 

# 查询所有
def select(table,filed):
    sql="select * from %s" %table
    utils.WriteLog(sql).info("select %s:" %sql)
    cur.execute(sql)
    res = cur.fetchall()
    if res:
       user = [{k:row[i] for i,k in enumerate(filed)} for row in res]
       result = {'code':0,'msg':user}
    else:
       result = {'code':1,'errmsg':'data is null'}
    return result 

# 更新
def update(table,filed,data):
    result=['%s = "%s"' %(k,data[k]) for k in data]
    sql ="update %s set %s where id = %s"%(table,','.join(result),data['id'])
    utils.WriteLog(sql).info("update %s:" %sql)
    res = cur.execute(sql)
    print res
    if res:
         res = {'code':0,'msg':'update sucessfor'}
    else:
         res = {'code':1,'errmsg':'update failed'}
    return res


# 删除
def delete(table,filed,data):
    sql = "delete from %s where id = %s" %(table,data['id'])
    utils.WriteLog(sql).info("delete %s:" %sql)
    res=cur.execute(sql)
    if res:
        res = {'code':0,'msg':'delete secussfor'}
    else:
        res = {'code':1,'errmsg':'delete failed'}
    return res
