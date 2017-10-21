#!/bin/env python
#coding=utf-8
#数据库功能函数

# 导入MySQLdb模块
import MySQLdb as mysql

# 连接数据库
conn = mysql.connect(host='121.43.191.76',user='root',passwd='123456',db='taoyake',port=3306,charset='utf8')
# 如果使用事务引擎，可以设置自动提交事务，或者在每次操作完成后手动提交事务
conn.autocommit(True)
# 创建游标
cur = conn.cursor()


# 注册用户函数
def insert(table,field,data):
    # 拼接插入的insert sql语句
    sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
    # 执行插入命令,并且把返回值赋一个变量
    res = cur.execute(sql)
    print res
    if res:
        result = {'code':0,'msg':'insert ok'}
    else:
        result = {'code':0,'msg':'insert fail'}
    return result

# 获取所有用户信息函数
def getlist(table,field):
    sql = "select * from %s" % table
    cur.execute(sql)
    res = cur.fetchall()
    if res:
        user = [{k:row[i] for i,k in enumerate(field)} for row in res]
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'errmsg':'data is null'}
    return result

# 获取单个用户信息函数
def getone(table,field,data):
    if data.has_key("username"):
        sql = 'select * from %s where username="%s"' % (table,data['username'])
    else:
        sql = 'select * from %s where id = "%s"' % (table,data['id'])
    print sql
    cur.execute(sql)
    res = cur.fetchone()
    print res
    if res:
        user = {k:res[i] for i,k in enumerate(field)}
        result = {'code':0,'msg':user}
    else:
        result = {'code':1,'msg':"data is null"}
    return result

# 更新用户信息函数
def update(table,field,data): 
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id=%s" %(table,','.join(conditions),data['id'])
    print sql 
    res = cur.execute(sql)
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result

#删除用户信息函数
def drop(id,sql):
    # 删除用户
    res = cur.execute(sql)
    if res:
        return True
    else:
        return 'del %s not exists'%(id)
