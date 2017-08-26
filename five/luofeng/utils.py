#!/usr/bin/env python 
# File Name: utils.py
# _*_ coding: utf-8 _*_
# Author: luofeng
# Mail: 18210085737@139.com 
# Blog: https://www.liyanlan.com 
import MySQLdb

# Determine whether the user has been registered
def user_regis(username):
	db = MySQLdb.connect('10.45.15.227','flask','FlaskWeb','reboot15',charset='utf8')
	cursor = db.cursor()
	sql = 'select * from user where username = "{0}"'.format(username)
	try:
		cursor.execute(sql)
		result = cursor.fetchone()
		ret = 0
		if username == result[1]:
			ret = 1
			return ret

	except:
		return "abnormal error"

	finally:
		db.close()

# Determine user login 
def user_login(phone,password):
	db = MySQLdb.connect('10.45.15.227','flask','FlaskWeb','reboot15',charset='utf8')
	cursor = db.cursor()
	sql = 'select * from user where phone = {0}'.format(phone)
	try:
		cursor.execute(sql)
		result = cursor.fetchone()
		ret = 0
		if phone != str(result[5]):
			return ret
		else:
			ret = 1
			if password == result[2]:
				return ret
			else:
				return "password error, login exception."
	except:
		return "abnormal data"

	finally:
		db.close()

# Determine Whether user has been admin  
def user_role(role):
	db = MySQLdb.connect('10.45.15.227','flask','FlaskWeb','reboot15',charset='utf8')
	cursor = db.cursor()
	sql = 'select * from user where role = {0}'.format(role)
	try:
		cursor.execute(sql)
		result = cursor.fetchone()
		if role == str(result[7]):
			return "User {0} is superad ministrator".format(result[1])
	
	except:
		return "abnormal data"

	finally:
		db.close()

# insert data to database
def db_insert(username,phone,password):
	db = MySQLdb.connect('10.45.15.227','flask','FlaskWeb','reboot15',charset='utf8')
	cursor = db.cursor()
	sql = "insert into user(username,password,sex,age,phone,email,role) values('%s','%s',0,20,'%s','user@reboot.cn',0)" %(username,password,phone)
	try:
		cursor.execute(sql)
		db.commit()
		return "User {0} is register success.".format(username)

	except:
		db.rollback()
		return "abnormal data"

	finally:
		db.close()

# delete data to database
def db_delete(uid):
	db = MySQLdb.connect('10.45.15.227','flask','FlaskWeb','reboot15',charset='utf8')
	cursor = db.cursor()
	sql = "delete from user where uid = {0}".format(uid)
	try:
		cursor.execute(sql)
		db.commit()

	except:
		db.rollback()
		return "abnormal data"

	finally:
		db.close()

# select data to database
def db_select(uid):
	db = MySQLdb.connect('10.45.15.227','flask','FlaskWeb','reboot15',charset='utf8')
	cursor = db.cursor()
	sql = "select * from user where uid = {0}".format(uid)
	try:
		cursor.execute(sql)
		result = cursor.fetchone()
		return result

	except:
		db.rollback()
		return "abnormal data"

	finally:
		db.close()

# select all data to database
def db_update(username,password,sex,age,phone,email,role,uid):
	db = MySQLdb.connect('10.45.15.227','flask','FlaskWeb','reboot15',charset='utf8')
	cursor = db.cursor()
	sql = "update user set username='%s',password='%s',sex='%s',age='%s',phone='%s',email='%s',role='%s' where uid = %s" %(username,password,sex,age,phone,email,role,uid)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
		return "abnormal data"

	finally:
		db.close()

# select all data to database
def db_select_all():
	db = MySQLdb.connect('10.45.15.227','flask','FlaskWeb','reboot15',charset='utf8')
	cursor = db.cursor()
	sql = "select * from user"
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		return result

	except:
		db.rollback()
		return "abnormal data"
	finally:
		db.close()
