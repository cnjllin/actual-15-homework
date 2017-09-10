#! /bin/env python
#coding:utf-8

import MySQLdb as mysql

import sys
reload(sys)
sys.setdefaultencoding('utf8')

conn= mysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='reboot15',charset='utf8')
conn.autocommit(True)
cur=conn.cursor()







def getone(table,field,data):
    if data.has_key("username"):
        sql='select * from %s  where username="%s"' % (table,data['username'])
    else:
        sql='select * from %s  where id=%s' % (table,data['id'])
    cur.execute(sql)
    res=cur.fetchone()
    if res:
        print res
        user={k:res[i] for i,k in enumerate(field)}
        result={'code':0,'msg':user}
    else:
        result={'code':1,'msg':"该用户未注册，无法登陆"}
    return result    	    			




##添加用户的函数，注册时调用
def insert (table,data):
    fields,values=[],[]
    for k,v in data.items():
        fields.append(k)
        values.append("'%s'" % v)
    sql="insert into %s (%s) value (%s)" % (table,','.join(fields),','.join(values))
    cur.execute(sql)
    result={'code':0,'errmsg':'ok'}
    return result

##删除用户的函数，删除时调用
def delete (table,uid):
    sql="delete from %s where id =%s" % (table,uid)
    cur.execute(sql)
    result={'code':0,'errmsg':'ok'}
    return result

##更新用户信息的函数，更新时调用
def updateid (table,data):
    conditions=[]
    for k,v in data.items():
        if v:
            conditions.append("%s='%s'" % (k,v)) 
    sql="update %s set %s where id =%s" % (table,','.join(conditions),data['id'])
    res=cur.execute(sql)
    if res:    	
        result={'code':0,'msg':'ok'}
    else:
        result={'code':1,'msg':'更新不成功'}	    	
    return result





##查看所有用户信息函数，用户列表页面时调用
def list(table,field):
    sql="select * from %s " % table
    cur.execute(sql)
    res=cur.fetchall()
    if not res:
        result={'code':1,'errmsg':'data is null'}
        return result
    else:
        user=[{k:row[i] for i,k in enumerate(field)} for row in res]
        return user


