#!/usr/bin/env python
#-*- coding:utf-8 -*-

#-----------------------------------
#     FileName: CMDB.py
#         Desc:
#       Author: copy
#      Version:
#     CreatTime: 2017-09-02
# ----------------------------------
# 
import MySQLdb as mysql

conn=mysql.connect(host="127.0.0.1",user="root",passwd="",db="reboot15",port=3306,charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

def trysql(sql):
    try:
        cur.execute(sql)
        result=cur.fetchone()
        if result:
            code =1
        else:
            code=0
        return code
    except Exception as e:
        code =2
        return code
    finally:
        conn.close

def register(data):
    print data['username']
    sql = 'select * from user where username=%s;' %(data['username'])
    insert_sql = "insert into user (%s) values (%s)" %(','.join(data.keys()),','.join(data.values()))
    if trysql(sql)==0:
        cur.execute(insert_sql)
        res = {'code':0,'msg':'register ok'}
    else:
        res = {'code':1,'msg':'user exsit!'}
    return res

def login(data):
    fields = ['username','password']
    sql = 'select username,password from user where username="%s";'% (data['username'])
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        user_dict = {k:result[i] for i,k in enumerate(fields)}
        if data['password'] == user_dict['password']:
            res = {'code':0,'msg':'login success'}
        else:
            res = {'code':1,'msg':'password wrong'}
    else:
        res = {'code':1,'msg':'user not exist'}
    return res

def role(data):
    sql = 'select role from user where username="%s";'(data['username'])
    cur.execute(sql)
    role = cur.fetchone()
    return role

def userlist():
    fields = ['id','username','password','role']
    sql = "select * from user;"
    cur.execute(sql)
    result = cur.fetchall()
    if not result:
        res = {'code':1,'errmsg':'data is null'}
    else:
        res = [{ k:row[i] for i,k in enumerate(field) for row in user }]
    return res

def getuser(data):
    fields = ['id','username','password','role']
    sql = "select * from user where id=%s" % (data['id'])
    cur.execute(sql)
    res = cur.fetchone()
    if not result:
        res = {'code':1,'errmsg':'data is null'}
    else:
        res = {k:result[i] for i,k in enumerate(fields)}
    return res

def update(table,field,data):
    condition = [ "%s = '%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id=%s" %(table,','.join(conditions),data['id'])
    cur.execute(sql)
    result = cur.fetchone()
    if not result:
        res = {'code':0,'msg':'update success'}
    else:
        res = {'code':1,'msg':'update failed'}
    return res

def delete(data):
    sql = 'delete form user where id=%s;'%(data['id'])
    cur.execute(sql)

cur.close()
conn.close()
