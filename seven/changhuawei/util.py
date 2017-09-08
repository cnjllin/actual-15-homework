#!/usr/bin/env python
#coding:utf-8


import MySQLdb as mysql
db = mysql.connect(host='127.0.0.1',user='root',passwd='123456',db='reboot15',port=3306,charset='utf8')
db.autocommit(True)
cur = db.cursor()

# 注册
def insert(table,filed,user):    
    sql = "insert into %s (%s) values (%s)" % (table,','.join(filed),','.join(['"%s"' % user[x] for x in filed]))
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'insert ok'}
    else:
        result = {'code':1,'msg':'insert fail'}
    # print res
    return result

# 登录

def getone(table,filed,user):
    if user.has_key("username"):
        # print user['username']
        sql = 'select * from %s where username = "%s"' %(table,user['username'])
    else:
        sql = 'select * from %s where id = "%s"' %(table,user['id'])
    # print sql
    cur.execute(sql)
    res = cur.fetchone()
    # print res
    if res:
        user = {k:res[i] for i,k in enumerate(filed)}
        # print user
        result = {'code': 0,'msg':user}
    else:
        result = {'code': 1,'msg':'user is null'}
    return result

def getlist(table,filed):
    sql = "select * from %s" % table
    cur.execute(sql)
    res = cur.fetchall()
    if res:
        user = [{k:row[i] for i,k in enumerate(filed)} for row in res]
        # user = [dict((k,row[i]) for i,k in enumerate(fileds))for row in ss]
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'errmsg':'user is null'}
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




