#!/usr/bin/env python
# --*-- coding:UTF-8 --*--
import MySQLdb as mysql


conn = mysql.connect(host='localhost',user='root',passwd='',port=3306,db='51reboot',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

def insert(table,field,data):
    sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'insert ok'}
    else:
        result = {'code':1,'msg':'insert fail'}
    return result

def delete(table,uid):
    sql='delete  from user where id=%s' % uid
    cur.execute(sql)

def update(table,field,data):
    condition = ["%s='%s'"%(k,data[k]) for k in data]
    sql = "update %s set %s where id='%s';"%(table,','.join(condition),data['id'])
    res=cur.execute(sql)
    if  res:
        result = {'code':0,'msg':'update ok'}
    else:
       result = {'code':1,'msg':'update fail'}
    return result 

def list(table,field):
    sql = 'select * from %s' % table
    cur.execute(sql)
    res=cur.fetchall()
    if not res:
        result = {'code':1,'errmsg':'data is null'}
    else:
        users=[dict((k,row[i]) for i,k in enumerate(field)) for row in res]
        result = {'code':0,'msg':users}
        return result

def getone(table,field,uid):
    sql='select %s from %s where id=%s' % (','.join(field),table,uid)
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        result={'code':1,'errmsg':'data is null'}
    else:
       user=[dict((k,res[i]) for i,k in enumerate(field))]
       result = {'code':0,'msg':user}
    return result

def getrole(table,uname):
    if checkout_user_exist(uname):
        sql = "select role from %s where u_name='%s'" % (table,uname)
        cur.execute(sql)
        result=cur.fetchone()
        res=result[0]
        return res

def getid(table,uname):
    if checkout_user_exist(uname):
        sql = "select id from %s where u_name='%s'" % (table,uname)
        cur.execute(sql)
        result=cur.fetchone()
        res=result[0]
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
