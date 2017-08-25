#/bin/env python
#coding=utf-8
#------------------------------------
#      FileName: util.py
#          Desc:
#        Author: liuyang
#       Version:
#    CreateTime: 2017-08-21
#------------------------------------

# 定义统计日志函数（传参 1.文件 2.访问top,默认10）

import MySQLdb as mysql
conn=mysql.connect(host='127.0.0.1',user='root',passwd='piptest',db='liuyang',port=6666,charset='utf8')
conn.autocommit(True)
cur=conn.cursor()

# 定义获取用户字典函数
def userlist():
	temp_list=[]
	user_keys= ['id','username','password']
	sql = "select id,username,password from user;"
	cur.execute(sql)
	user_values = cur.fetchall()
	for i in user_values:
		temp_dict = dict(zip(user_keys,i))
		temp_list.append(temp_dict)
	return temp_list

# 定义注册判断用户&密码函数
def registorcheck(**user_dict):
	user_list=userlist()
	#print user_list
	name_list=[]
	res_code = {'code':'0','msg':''}
	for i in user_list:
		name_list.append(i["username"])
	if user_dict['username'] in name_list:
		res_code['code'] = 1
		res_code['msg'] = 'User exist !'
	else:
		res_code['code'] = 0
		res_code['msg'] = 'Registor ok !'
	return res_code

# 定义登录判断用户&密码函数
def logincheck(username,password):
	user_list=userlist()
	#[{'username': u'liuyang', 'password': u'12', 'id': 1L}, {'username': u'liu', 'password': u'12', 'id': 2L}, {'username': u'aa', 'password': u'12', 'id': 3L}]
	print user_list
	res_code = {'code':'0','msg':''}
	for i in user_list:
		print i
		print i['username'],i['password']
		if username == i['username']:
			if password == i['password']:
				res_code['code'] = 0
				res_code['msg'] = 'Login sucessfully !'
			else:
				res_code['code'] = 1
				res_code['msg'] = 'Wrong password,please confirm !'
			return res_code
		else:
			continue
	res_code['code'] = 2
	res_code['msg'] = 'User not exist !'
	return res_code

