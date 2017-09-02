#!/usr/bin/env python
# --*-- coding:UTF-8 --*--
import MySQLdb as mysql


conn = mysql.connect(host='localhost',user='root',passwd='',port=3306,db='51reboot',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

def insert(table,field,*data):
    data2=[]
    for x in data:
       data2.append("'%s'" % x)
    sql = 'insert into %s (%s) values (%s)' % (table , ','.join(field) , ','.join(data2))
    cur.execute(sql)

def delete(table,uid):
    sql='delete  from user where id=%s' % uid
    cur.execute(sql)

def update(table,field,_value,uid):
    u=getone(table,field,uid)
    if u:
        u1=[]
        for v in _value:
            u1.append("'%s'" % v)
        u2=zip(field,u1)
        u3=['%s=%s' % (item[0],item[1]) for item in u2]
        sql='update %s set %s where id=%s' % (table,','.join(u3),uid)
        cur.execute(sql)     
        return getone(table,field,uid)

def list(table,field):
    sql = 'select * from %s' % table
    cur.execute(sql)
    res=cur.fetchall()
    if not res:
        result = {'code':1,'errmsg':'data is null'}
        return result
    else:
        users=[dict((k,row[i]) for i,k in enumerate(field)) for row in res]
        return users

def getone(table,field,uid):
    sql='select %s from %s where id=%s' % (','.join(field),table,uid)
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        result={'code':1,'errmsg':'data is null'}
        return result
    else:
       user=dict((k,res[i]) for i,k in enumerate(field))
       users=[]
       users.append(user)
       return users

def getrole(table,uname):
    sql = "select role from %s where u_name='%s'" % (table,uname)
    print sql
    cur.execute(sql)
    result=cur.fetchone()
    res=result[0]
    print res
    return res

def getid(table,uname):
    sql = "select id from %s where u_name='%s'" % (table,uname)
    cur.execute(sql)
    result=cur.fetchone()
    res=result[0]
    print res
    return res

def GetUser():
    filed=['u_name','password']
    sql='select %s  from user' %  (','.join(filed))
    cur.execute(sql)
    s=cur.fetchall()
    user_info=dict((row[0],row[1])  for row in s)
    return user_info


def checkout_user_pass(u, p):
    user = GetUser()
    if u in user.keys():
        if user[u] == p:
            return True

        else:
            return False

    else:
        return False


def checkout_user_exist(u):
    user = GetUser()
    if u in user.keys():
        return True
    else:
        return False
