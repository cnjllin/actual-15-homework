import MySQLdb as mysql
from flask import Flask,request,render_template,redirect
db=mysql.connect(host="192.168.50.160",user="root",passwd="zhaoxf513",db="reboot15",port=3306,charset='utf8')
db.cursor()
cur = db.cursor()
db.autocommit(True)
app = Flask(__name__)

def usercheck(**dict_reg):
    sql = "select username from user;"
    cur.execute(sql)
    namelist = cur.fetchall()
    code_msg = {'code':'1','msg':''}
    if dict_reg['username'] in namelist:
        code_msg['msg'] = 'User is already exist '
        code_msg['code'] = '0'
    else:
        sql_insert = "INSERT INTO user(username,password,role) VALUE ('%s','%s',%s);" %(dict_reg['username'],dict_reg['password'],int(dict_reg['role']))
        cur.execute(sql_insert)
        print sql_insert
        code_msg['msg'] = 'Sign up success!'
    return code_msg

def logincheck(name,passwd,sql):
    cur.execute(sql)
    list = cur.fetchall()
    userdict = {}
    namelist = []
    mes = {'code': '0', 'msg': ''}
    for i in list:
        b = i[0]
        c = i[1]
        userdict[b] = c
    # print userdict
    for a in userdict:
        namelist.append(a)
    # print namelist
    # print userdict.get(name)
    if name in namelist:
        if passwd == userdict.get(name):
            mes['code'] = 1
        else:
            mes['code'] = 2
            mes['msg'] = 'your password is not right!'
    else:
        mes['code'] = 0
        mes['msg'] = 'your username is not exist!'
    return mes

def admcheck(sql_ch):
    cur.execute(sql_ch)
    list = cur.fetchone()
    role = list[0]
    return role




def userlist(sql):
    cur.execute(sql)
    list = cur.fetchone()
    col_list = ['id','username', 'password', 'role']
    user_dict = dict((k,list[i]) for i,k in enumerate(col_list))
    return user_dict

def admlist(sql_list):
    cur.execute(sql_list)
    list = cur.fetchall()
    col_list = ['id', 'username', 'password', 'role']
    user_list = [dict((k, v[i]) for i, k in enumerate(col_list)) for v in list]
    return user_list

def update(sql_update,id):
    cur.execute(sql_update)
    sel_list = "select * from user where id = '%s'" %id
    cur.execute(sel_list)
    if cur.execute(sel_list) :
        msg = 'update success!'
    else:
        msg = 'something wrong'
    return  msg

def delete(sql):
    cur.execute(sql)
    id = cur.fetchone()
    sql_delete = "'DELETE FROM user where id='%s';" % (id[0])
    cur.execute(sql_delete)
    if cur.execute(sql_delete):
        msg = 'delete success'
    else:
        msg = 'delete wrong'
    return msg
