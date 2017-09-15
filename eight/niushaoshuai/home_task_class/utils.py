#!/usr/bin/env python
# --*-- coding:UTF-8 --*--
import MySQLdb as mysql
import config

conn = mysql.connect(
        host = config.host ,
        user = config.user,
        passwd = config.passwd,
        db = config.db,
        port = config.port,
        charset = config.charset)
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
    sql="delete  from %s where id=%s" % (table,uid)
    cur.execute(sql)

def update(table,data):
    condition = ["%s='%s'"%(k,data[k]) for k in data]
    sql = "update %s set %s where id='%s';"%(table,','.join(condition),data['id'])
    res=cur.execute(sql)
    if  res:
        result = {'code':0,'errmsg':'update ok'}
    else:
       result = {'code':1,'errmsg':'update fail'}
    return result 

def update_passwd(table,id,data):
    new_pwd=data['newpasswd'][0]
    old_pwd=data['oldpasswd'][0]
    if new_pwd != old_pwd :
        sql = "update %s set password='%s' where id='%s';"%(table,new_pwd,id)
        res=cur.execute(sql)
        if  res:
            result = {'code':0,'errmsg':'update ok'}
        else:
            result = {'code':1,'errmsg':'update fail'}
    else:
        result = {'code':1,'errmsg':'two password is the same'}
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

def getone(table,field,data):
    if data.has_key('id'):
        sql='select %s from %s where id=%s' % (','.join(field),table,data['id'])
    else:
        sql='select %s from %s where username="%s"' % (','.join(field),table,data['username'])
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        result={'code':1,'errmsg':'data is null'}
    else:
       user=dict((k,res[i]) for i,k in enumerate(field))
       result = {'code':0,'msg':user}
    return result

def getrole(table,uname):
    if checkout_user_exist(uname):
        sql = "select role from %s where username='%s'" % (table,uname)
        cur.execute(sql)
        result=cur.fetchone()
        res=result[0]
        return res

def getid(table,uname):
    if checkout_user_exist(uname):
        sql = "select id from %s where username='%s'" % (table,uname)
        cur.execute(sql)
        result=cur.fetchone()
        res=result[0]
        return res

def GetUser():
    filed=['username','password']
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
