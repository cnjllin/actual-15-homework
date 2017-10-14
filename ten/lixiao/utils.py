#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
import config,util
import traceback

con=mysql.connect(host=config.DB_host,user=config.DB_user,passwd=config.DB_passwd,db=config.DB_db,port=config.DB_port,charset=config.DB_charset)
con.autocommit(True)
cur = con.cursor()

#insert注册
def regist(table,field,data):
    sql = 'insert into %s (%s) values(%s)' %(table,','.join(field),','.join(['"%s"' %data[v] for v in field]))
    print sql
    try:
        res = cur.execute(sql)
        result = {'code':0,'msg':'reg success'}
    except:
        result = {'code':1,'msg':'reg faild'}
        util.Writelog('err').error('Execute %s error: %s' %(sql,traceback.format_exc()))
    return result
    

#select单用户查询
def getone(table,field,data):
    if data.has_key('username'):
        sql = "select * from %s where username='%s'" %(table,data['username'])
    elif data.has_key('sr'):
        sql = "select * from %s where sr='%s'" %(table,data['sr'])
    else:
        sql = "select * from %s where id='%s'" %(table,data['id'])
    try:
        cur.execute(sql)
        res=cur.fetchone()
        user = {k:res[i] for i,k in enumerate(field)}
        result = {'code':0,'msg':user}
    except:
        result = {'code':1,'msg':'user not is exist'}
        util.Writelog('err').error('Execute %s error: %s' %(sql,traceback.format_exc()))
    return result


#select多用户查询
def getall(table,field):
    sql = "select * from %s" %(table)
    print sql
    util.Writelog('sql').info('getall:%s' %sql)
    try:
        cur.execute(sql)
        res = cur.fetchall()
        user = [{k:row[i] for i,k in enumerate(field)} for row in res]
        result = {'code':0,'msg':user}
    except:
        result = {'code':1,'msg':'select faild'}
        util.Writelog('err').error('Execute %s error: %s' %(sql,traceback.format_exc()))
    return result

#数据更新
def update(table,field,data):
    sql = "update %s set %s where id=%s" %(table,','.join(["%s='%s'" %(k,data[k]) for k in data]),data['id'])
    try:
        res = cur.execute(sql)
        result = {'code':0,'msg':'update success'}
    except:
        result = {'code':1,'msg':'update faild'}
        util.Writelog('err').error('Execute %s error: %s' %(sql,traceback.format_exc()))
    return result

#删除用户
def delete(user,uid):
    sql = "delete from %s where id=%s" %(user,uid)
    try:
        res = cur.execute(sql)
        result = {'code':0,'msg':'delete success'}
    except:
        result = {'code':1,'msg':'delete faild'}
        util.Writelog('err').error('Execute %s error: %s' %(sql,traceback.format_exc()))
    return result
