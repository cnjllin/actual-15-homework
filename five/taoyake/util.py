#/usr/bin/python
# -*- coding: utf-8 -*-

#导入MySQLdb模块
import MySQLdb as mysql

def connect():
    try:
        con = mysql.connect(host="localhost",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')
        con.autocommit(True)
        cur = con.cursor()
    except Exception as e:
            print e
    return cur

def select(sql):
    cur = connect()
    cur.execute(sql)
    data = cur.fetchall()
    return data

def chk_login(username,password,sql):
    # 登录验证
    cur = connect()
    cur.execute(sql)
    data = cur.fetchone()
    if data[1] == username and data[2] == password:
        return True
    else:
        return "user %s or password is error." % (username)


def insert(sql,args=()):
    cur = connect()
    sql_uniq = 'select username from user where username = "%s"' % (username)
    print sql_uniq
    cur.execute(sql_uniq)
    if not cur.fetchone():
        cur.execute(sql)
        return True
    else:
        print 'user %s already exist'%(username)

def del_user(uid,sql):
    # 删除用户
    cur = connect()
    cur.execute(sql)
    if cur.rowcount == 1:
        return True
    else:
        return 'del %s not exists'%(uid)
