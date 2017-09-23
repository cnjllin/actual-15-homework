#!/usr/bin/env  python
#coding:utf-8
import MySQLdb as mysql
import config
import log_output

connect_db = mysql.connect(
user   =  config.db_user,passwd =  config.db_passwd,db     =  config.db_name ,host   =  config.db_host,charset=  "utf8" )
cur = connect_db.cursor()

def insert_sql(table_name,field,data):
    sql = "INSERT INTO %s (%s) VALUES (%s);" % (table_name, ','.join(field), ','.join(['"%s"' % data[x] for x in field]))
    log_output.WriteLog("SQL").info("Insert:%s" % sql)
    res = cur.execute(sql)
    connect_db.commit()
    if  res:
        result = {'code':0,'msg':'insert ok'}
    else:
        result = {'code':1,'msg':'insert fail'}
    return result

def list(table_name,field):
    sql = "select  *  from %s ;" % table_name
    cur.execute(sql)
    res = cur.fetchall()
    log_output.WriteLog("SQL").info("Select:%s" % sql)
    if res:
        user = [dict((k,row[i]) for i,k in enumerate(field))for row in res]
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'errmsg':'data is null'}

    return  result

def getone(table,data,field):
    if data.has_key('username'):
        sql = 'select * from %s where username="%s";' % (table,data['username'])
    else:
        sql = 'select %s  from %s where id="%s";' % (','.join(field),table,data['id'])
    cur.execute(sql)
    res = cur.fetchone()
    log_output.WriteLog("SQL").info("Getone:%s" % sql)
    if res:
        user = {k:res[i] for i,k in enumerate(field)}
        result  = {'code':0,'msg':user}
    else:
        result ={'code':1, 'msg':"data is null"}
    return result 

def _update(table,field,data): 
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id=%s ;" %(table,','.join(conditions),data['id'])
    res = cur.execute(sql)
    log_output.WriteLog("SQL").info("Update:%s" % sql)
    if res :
        connect_db.commit()
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'Update fail'}
    return result 


def _delete(table_name,data):
    tag=False
    try:
        sql = 'delete from %s where id="%s" ;' % (table_name,data['id'])
        if  cur.execute(sql):
            connect_db.commit()
            log_output.WriteLog("SQL").info("Delete:%s" % sql)
            tag=True
    except Exception, e:
        print 'Error %s' % (sql)
    return   tag

def check(table,field,where):
    if isinstance(where, dict) and where:
        conditions = []
        for k,v in where.items():
            conditions.append("%s='%s'" % (k, v))
    sql = "select %s from %s where %s ;" % (','.join(field),table,' AND '.join(conditions))
    try:
        if  cur.execute(sql):
            res = cur.fetchone()
            log_output.WriteLog("SQL").info("Check:%s" % sql)
            user =  {k:res[i] for i,k in enumerate(field)}
            result  = {'code':0,'msg':user}
        else:
            result ={'code':1, 'msg':"data is null"}
    except Exception, e:
        result ={'code':1, 'msg':"SQL Error "}

    return  result
