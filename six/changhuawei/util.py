#!/usr/bin/env python
#coding:utf-8


import MySQLdb as mysql
db = mysql.connect(host='127.0.0.1',user='root',passwd='123456',db='reboot15',port=3306,charset='utf8')
db.autocommit(True)
cur = db.cursor()

# 注册
def _reg(data):    
    fileds = []
    values = []
    for k,v in data.items():
        fileds.append(k)
        values.append("'%s'" % v)
    sql = "insert into user ({}) values ({})".format(','.join(fileds),','.join(values))
    # print sql
    cur.execute(sql)

# 登录
def _login(data):
    sql = "select * from  user where username = '{}'".format(data['username'])
    # print sql
    cur.execute(sql)
    res = cur.fetchone()
    return res



# 查询所有
def _select_all():
    sql = "select * from user"
    # print sql
    cur.execute(sql)
    ss = cur.fetchall()
    fileds = ['id','username','password','role','email']
    res = [dict((k,row[i]) for i,k in enumerate(fileds))for row in ss]
    # print res
    return res

# 查询单个
def _select_name(data):
    fileds = ['id','username','password','role','email']
    res = []
    sql = "select * from user where username = '{}'".format(data.values()[0])
    # print sql
    cur.execute(sql)
    ss = cur.fetchone()
    if ss == None:
        res = ss
        return res
    else:
        user_info = dict(zip(fileds,ss))
        res.append(user_info)
        # print res
        return res

# 删除用户
def _delete(data):
    sql = "delete from user where id = '{}'".format(data['id'])
    print sql
    cur.execute(sql)

# 更新信息
def _update(data):
    fileds = ["{}='{}'".format(k,data[k]) for k in data]
    sql = "update user set {} where id = '{}'".format(','.join(fileds),data['id'])
    cur.execute(sql)
    ss = cur.fetchone()
    return ss


