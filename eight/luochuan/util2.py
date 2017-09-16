import MySQLdb as mysql
from flask import Flask,request,render_template,redirect,session
db=mysql.connect(host="192.168.62.1",user="root",passwd="zhaoxf513",db="reboot15",port=3306,charset='utf8')
db.cursor()
cur = db.cursor()
db.autocommit(True)
app = Flask(__name__)
field = ['id', 'username', 'password', 'role']
table = 'user'

def usercheck(table_name,**dict_reg):
    sql_insert = "INSERT INTO %s(username,password,role) VALUE ('%s','%s',%s);" % (table_name,dict_reg['username'], dict_reg['password'], int(dict_reg['role']))
    res = cur.execute(sql_insert)
    code_msg = {'code':'1','msg':''}
    if res:
        code_msg['msg'] = 'Sign up success!'
    else:
        code_msg['msg'] = 'User is already exist '
        code_msg['code'] = '0'
    return code_msg

def logincheck(name,passwd):
    field = ['id','username','password','role']
    sql = "select * from user where username = '%s';" %name
    res = cur.execute(sql)
    list = cur.fetchone()
    mes = {}
    if res:
        userdict = {k: list[i] for i, k in enumerate(field)}
        if passwd == userdict.get('password'):
            mes = userdict
            mes['code'] = 1
            mes['msg'] = 'login success!'
        else:
            mes['code'] = 2
            mes['msg'] = 'your password is not right!'
    else:
        mes['code'] = 0
        mes['msg'] = 'your username is not exist!'
    return mes
#
#
def getone(name):
    sql = "select * from user where username = '%s';" %name
    cur.execute(sql)
    list = cur.fetchall()
    print list
    col_list = ['id','username', 'password', 'role']
    user_list = [dict((k, v[i]) for i, k in enumerate(col_list)) for v in list]
    print user_list
    return user_list

def admlist():
    sql_list = "select * from user;"
    cur.execute(sql_list)
    list = cur.fetchall()
    col_list = ['id', 'username', 'password', 'role']
    user_list = [dict((k, v[i]) for i, k in enumerate(col_list)) for v in list]
    return user_list

def userinfo(data):
    sql = "select * from user where id = '%s';" %data['id']
    res = cur.execute(sql)
    print sql
    list = cur.fetchone()
    col_list = ['id', 'username', 'password', 'role']
    user_dict = {k:list[i] for i, k in enumerate(col_list)}
    print user_dict
    if res:
        user_dict['code'] = 1
    else:
        user_dict['code'] = 0
    return user_dict
#
def update(data):
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    print conditions
    sql = "update user set %s where id=%s" %(','.join(conditions),data['id'])
    print sql
    res = cur.execute(sql)
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'msg':'update fail'}
    return result


def delete(table,data):
    sql = 'DELETE FROM %s where id="%s" ;' % (table,data['id'])

    if  cur.execute(sql):
        result = 1
    else:
        result = 0
    print result
    return result



