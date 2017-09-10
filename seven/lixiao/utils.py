#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
con=mysql.connect(host="127.0.0.1",user="root",passwd="123456",db="reboot15",port
=3306,charset='utf8')
con.autocommit(True)
cur = con.cursor()



#insert数据
def insert(table,field,data):
    sql = 'insert into %s (%s) values(%s)' %(table,','.join(field),','.join(['"%s"' %v for i,v in data.items()]))
    res = cur.execute(sql)
    if res:
        res = {'code':0,'msg':"reg is ok"}
    else:
        res = {'code':1,'msg':"reg is fail"}
    return res

#根据username查单用户
def getone(table,field,data):
    if data.has_key('username'):
        sql = 'select * from %s where username = "%s"' %(table,data['username'])
    else:
        sql = 'select * from %s where id = "%s"' %(table,data['id'])
    cur.execute(sql)
    res = cur.fetchone()
    if res:
        user = {k:res[i] for i,k in enumerate(field)}
        result = {'code':0,'msg':user}
        return result
    else:
        resul = {'code':1,'msg':'input is wrong'}
    return result

#查询userlist所有用户
def getall(table,field):
    sql = 'select * from %s' %(table)
    cur.execute(sql)
    res = cur.fetchall()
    if res:
        user = [{k:row[i] for i,k in enumerate(field)} for row in res]
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'msg':'data is null'}
    return result


#删除用户
def dele(table,field,uid):
    sql = 'delete from %s where id=%s' %(table,uid)
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'delete ok'}
    else:
        result = {'code':1,'errmsg':'delete fail'}
    return result

#更改用户
def update(table,field,data):
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id='%s'" %(table,','.join(conditions),data['id'])
    print sql
    res = cur.execute(sql)
    print res
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result

