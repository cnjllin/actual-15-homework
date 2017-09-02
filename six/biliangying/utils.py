#!/usr/bin/python
#coding:utf-8
import MySQLdb as mysql
db=mysql.connect(host="127.0.0.1 ",user="root",passwd="123",db="reboot15",port=3306,charset='utf8')
db.autocommit(True)
cur = db.cursor()

# 注册
def insert(field,data):
	sql = "insert into user (%s) values (%s)" % (','.join(field),','.join(data))
	print sql
	cur.execute(sql)

# 判断用户是否存在
def judgeuser(user):
	sql = "select * from user where username='%s'" % user["username"]
        cur.execute(sql)
	res = cur.fetchall()
        if res:
                result = {'code':0,'errmsg':'exit'}
                return result
	else:
		result = {'code':1,'errmsg':'ok'}
                return result

# 登陆
def login(user):
	sql = "select * from user where username='%s' and password='%s'" % (user["username"],user["password"])
	cur.execute(sql)
        res = cur.fetchall()
        if res:
                result = {'code':0,'errmsg':'right'}
                return result
        else:
                result = {'code':1,'errmsg':'error'}
                return result
# 列表
def userlist():
        field = ['id','username','password','tel','email','role']
	sql = "select * from user"
        cur.execute(sql)
        res = cur.fetchall()
	if not res:
                result = {'code':0,'errmsg':'data is null'}
               	return result
       	if res:
               	user = [{k:row[i] for i,k in enumerate(field)}for row in res]
               	return user

# 查询用户信息
def inquire(uid):
	sql = "select * from user where id=%s" % uid
	cur.execute(sql)
        res = cur.fetchone()
	field = ['id','username','password','tel','email','role']
	if not res:
                result = {'code':0,'errmsg':'data is null'}
                return result
        if res:
                user = {k:res[i] for i,k in enumerate(field)}
                return user
		
# 更改用户信息
def update(user):
	conditions = ["%s='%s'" % (k,user[k]) for k in user]
	sql = "update user set %s where id = %s" % (','.join(conditions),user['id'])
	cur.execute(sql)
	print sql,conditions

# 删除用户
def delete(uid):
	sql = "delete from user where id=%s" % int(uid)
	cur.execute(sql)

# 判断角色
def role(user):
	sql = "select * from user where username='%s'" % user["username"]
	cur.execute(sql)
	res = cur.fetchone()
	print res
	if res[-1] == 0:
		result = {'code':0,'errmsg':'admin'}
		return result
	else:
		result = {'code':1,'errmsg':'user'}
		return result
