#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
db=mysql.connect(host="127.0.0.1 ",user="root",passwd="123",db="reboot15",port=3306,charset='utf8')
db.autocommit(True)
cur = db.cursor()

# 插入
def insert(table,field,data):
	sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
	res = cur.execute(sql)
	if res:
		result = {'code':0,'errmsg':'insert ok'}
                return result
        else:
                result = {'code':1,'errmsg':'insert fail'}
                return result

# 查询用户信息
def getone(table,data,field):
	if data.has_key("username"):
		sql = "select * from %s where username='%s'" % (table,data["username"])
	else:
		sql = "select * from %s where id=%s" % (table,data['id'])
	cur.execute(sql)
	res = cur.fetchone()
        if res:
		user = {k:res[i] for i,k in enumerate(field)}
                result = {'code':0,'msg':user}
                return result
	else:
		result = {'code':1,'msg':'data is null'}
                return result

# 列表
def userlist(table):
        field = ['id','username','password','tel','email','role']
	sql = "select * from %s" % (table)
        cur.execute(sql)
        res = cur.fetchall()
	if not res:
                result = {'code':0,'errmsg':'data is null'}
               	return result
       	if res:
               	user = [{k:row[i] for i,k in enumerate(field)}for row in res]
               	return user
		
# 更改用户信息
def update(table,field,data): 
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    sql = "update %s set %s where id=%s" %(table,','.join(conditions),data['id'])
    res = cur.execute(sql)
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result 

# 删除用户
def delete(table,uid):
	sql = "delete from %s where id=%s" % (table,int(uid))
	cur.execute(sql)
