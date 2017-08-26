# -*- coding: utf-8 -*-
import MySQLdb as mysql
dbut=mysql.connect(host="192.168.50.160",user="root",passwd="zhaoxf513",db="reboot15",port=3306,charset='utf8')
dbut.autocommit(True)
cur=dbut.cursor()


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


def usercheck(**reg_dict):
    sql = "select username from user;"
    cur.execute(sql)
    list=cur.fetchall()
    error_mes = {'code':'0','msg':''}
    namelist = []
    for i in list:
        b = ''.join(map(lambda x: "%c" % ord(x), i[0]))
        namelist.append(b)
    if reg_dict['username'] in namelist:
        error_mes['code'] = 1
        error_mes['msg'] = 'User is already exist '
    else:

        username = reg_dict['username']
        password = reg_dict['password']
        sex = reg_dict['sex']
        age = reg_dict['age']
        phone = reg_dict['phone']
        email = reg_dict['email']
        role = reg_dict['role']
    sql_insert = "INSERT INTO user(username,password,sex,age,phone,email,role) VALUES('%s','%s',%s,%s,%s,'%s',%s);"%(username,password,sex,age,phone,email,role)
    print sql_insert
    cur.execute(sql_insert)
    error_mes['code'] = 0
    return error_mes




def logincheck(user,passwd):
    sql = "select username,password from user;"
    cur.execute(sql)
    list = cur.fetchall()
    userdict = {}
    namelist = []
    mes = {'code': '0', 'msg': ''}
    for i in list:
        b = ''.join(map(lambda x: "%c" % ord(x), i[0]))
        c = ''.join(map(lambda x: "%c" % ord(x), i[1]))
        userdict[b] = c
    for a in userdict:
        namelist.append(a)
    if user in namelist:
        if passwd == userdict[user]:
            mes['code'] = 1
        else:
            mes['code'] = 2
            mes['msg'] = 'your password is not right!'
    else:
        mes['code'] = 0
        mes['msg'] = 'your username is not exist!'
    return mes