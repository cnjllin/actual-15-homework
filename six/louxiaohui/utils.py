#!/usr/bin/python
# -*- coding:utf-8 -*-
# **********************************************************
# * Author        : louxiaohui
# * Email         : 1031138448@qq.com
# * Last modified : 2017-08-28 04:24
# * Filename      : mysql.py
# * Description   : 
# * ********************************************************
import MySQLdb as mysql
import config
import hashlib
conn = mysql.connect(
        host = config.host ,
        user = config.user,
        passwd = config.passwd,
        db = config.db,
        port = config.port,
        charset = config.charset)
# set autocommit to True to enable the insert happened successfully
conn.autocommit(True)
# create a cursor
cur = conn.cursor()

def create_user(table_name,data):
    str = data.get('password')
    pass1 = hashlib.sha1(str).digest()
    pass2 = hashlib.sha1(pass1).hexdigest()
    pass3 = '*' + pass2.upper()
    data['password'] = pass3
    print data
    fields = []
    values = []
    for k,v in data.iteritems():
        fields.append(k)
        values.append("'%s'" %v)
    sql = "insert into %s (%s) values (%s)" %(table_name,",".join(fields),",".join(values))
    print sql
    try:
        cur.execute(sql)
    except Exception as e:
        print "sql: %s,error: %s" % (sql,e)
def convert_user_info_to_dict(table_name,id):
     field = ['id', 'username', 'password', 'sex', 'age', 'phone', 'email', 'role']
     sql = "select * from %s where id=%s" % (table_name,id)
     cur.execute(sql)
     user = cur.fetchone()
     print user
     result = dict(zip(field,user))
     print result
     return result
def update_user_info(table_name,data):
    flag = False
    str = data.get('password')
    pass1 = hashlib.sha1(str).digest()
    pass2 = hashlib.sha1(pass1).hexdigest()
    pass3 = '*' + pass2.upper()
    data['password'] = pass3
    print data
    data_new = ",".join(["%s='%s'"%(k,v) for k,v in data.iteritems()])
    sql = "update user set %s where id = %s" %(data_new,data['id'])
    print sql
    try:
        cur.execute(sql)
        flag = True
    except Exception as e:
        print "error: %s" %e
        flag = False
    return flag
    
def delete_user_info(table_name,id):
    flag = False
    sql = 'delete from %s where id = %s' % (table_name,id)
    try:
        cur.execute(sql)
        flag = True
    except Exception as e:
        print "error: %s" %e
        flag = False
    return flag

def get_all_user_info(table_name):
    sql = 'select * from %s' % table_name
    try:
        cur.execute(sql)
        user_data=cur.fetchall()
    except Exception as e:
        print "error: %s" %e
    return user_data
