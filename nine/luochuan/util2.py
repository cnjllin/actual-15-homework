import MySQLdb as mysql
import db_config,util
from flask import Flask,request,render_template,redirect,session
db=mysql.connect(db_config.host,db_config.user,db_config.passwd,db_config.db,db_config.port,db_config.charset)
db.cursor()
cur = db.cursor()
db.autocommit(True)
app = Flask(__name__)
field = ['id','username', 'password', 'role', 'email', 'phone']
table = 'user'

def useradd(table_name, field01, data):
    sql_insert = "INSERT INTO %s (%s) VALUES (%s);" % (table_name, ','.join(field01), ','.join(['"%s"' % data[x] for x in field01]))
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
    util.WriteLog('sql').info('select : %s' % sql)
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
    util.WriteLog('loginmes').info('userinfo  : %s' % mes)
    return mes
#
#
def getone(name):
    sql = "select * from user where username = '%s';" %name
    cur.execute(sql)
    list = cur.fetchone()
    col_list = ['id','username', 'password', 'role', 'email', 'phone']
    user_list = dict((k, list[i]) for i, k in enumerate(col_list))
    util.WriteLog('getone').info('getoneinfo  : %s' % user_list)
    return user_list

def admlist():
    sql_list = "select * from user;"
    cur.execute(sql_list)
    list = cur.fetchall()
    user_list = [dict((k, v[i]) for i, k in enumerate(field)) for v in list]
    util.WriteLog('sql').info('SELECT : %s' % sql_list)
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
def update(table,field,data):
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    print conditions
    sql = "update user set %s where id=%s" %(','.join(conditions),data['id'])
    util.WriteLog('updata_sql').info('updata : %s' % sql)
    res = cur.execute(sql)
    if res :
        result = {'code':0,'msg':'update success'}
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




