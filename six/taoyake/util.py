#!/bin/env python
#coding=utf-8
#数据库功能函数

import MySQLdb as mysql
conn = mysql.connect(host='localhost',user='root',passwd='123456',db='reboot15',port=3306,charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

# 定义检查sql函数
def trysql(sql):
        try:
                cur.execute(sql)
                result=cur.fetchone()
                if result:
                        code=1
                else:
                        code=0
                return code
        except Exception as e:
                code=2
                return code
        finally:
                conn.close

# 注册插入数据库
def register(data):
        print data['username']
        sql = 'select * from taokey where username=%s;' %(data['username'])
        insert_sql = 'insert into taokey (%s) values(%s);' %(','.join(data.keys()),','.join(data.values()))
        print insert_sql
        if trysql(sql)==0:
                cur.execute(insert_sql)
                res = {'code':0,'msg':'registor ok'}
        else:
                res = {'code':1,'msg':'User exsit !'}
        return  res

# 查询用户密码
def login(data):
        fields = ['username','password']
        sql = 'select username,password from taokey where username="%s";'%(data['username'])
        cur.execute(sql)
        result = cur.fetchone()
        if result:
                user_dict = {k:result[i] for i,k in enumerate(fields)}
                if data['username'] == user_dict['username']:
                        if data['password'] == user_dict['password']:
                                res = {'code':0,'msg':'login sucess'}
                        else:
                                res = {'code':1,'msg':'wrong passwd'}
        else:
                res = {'code':1,'msg':'user not exist'}
        return res

# 查询用户role(管理员/普通用户)
def role(data):
        sql = 'select role from taokey where username="%s";'%(data['username'])
        cur.execute(sql)
        role = cur.fetchone()
        return role

def userlist():
        fields = ['id','username','password','role']
        sql = 'select * from taokey;'
        cur.execute(sql)
        result = cur.fetchall()
        if not result:
                res = {'code':1,'msg':'data is null'}
        else:
                res = [{k:row[i] for i,k in enumerate(fields)} for row in result]
        return res


# 查询用户信息
def getuser(data):
        print data
        fields = ['id','username','password','role']
        sql = 'select * from taokey where id="%s";'%(data['id'])
        cur.execute(sql)
        result = cur.fetchone()
        if not result:
                res = {'code':1,'msg':'data is null'}
        else:
                res = {k:result[i] for i,k in enumerate(fields)}
        return res

def update(data):
        condition = ["%s='%s'"%(k,data[k]) for k in data]
        sql = 'update taokey set %s where id=%s;' %(','.join(condition),data['id'])
        cur.execute(sql)
        result = cur.fetchone()
        if not result:
                res = {'code':0,'msg':'update sucess'}
        else:
                res = {'code':1,'msg':'update failed'}
        return res

def delete(data):
        sql = 'delete from taokey where id=%s;'%(data['id'])
        cur.execute(sql)


#cur.close()
#conn.close()
