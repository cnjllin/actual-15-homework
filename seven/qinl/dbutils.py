#coding:utf-8
from apps import app
import pymysql as mysql


db_info = app.config.get('DB_INFO')
db_fiels = app.config.get('DB_FIELDS')

host = db_info.get('HOST')
user = db_info.get('USER')
passwd = db_info.get('PASSWD')
db = db_info.get('DB')
charset = db_info.get('CHARSET')

field = db_fiels.get('USER_FIELD')
user_field = db_fiels.get('VERIFY_USER')

db = mysql.connect(user=user,passwd=passwd,host=host,db=db,charset=charset)
cursor = db.cursor()

#校验用户名密码
def verify_user(tname,username,password,user_field):
    sql = "select %s from %s where username='%s';" %(','.join(user_field),tname,username)
    cursor.execute(sql)
    query_result = cursor.fetchone()

    if query_result:
        data = {v: query_result[k] for k, v in enumerate(user_field)}
        if username == data['username'] and password == data['password']:
            verify_result = {'username':data['username'], 'role':data['role'], 'status':data['status'],'phone':data['phone'],'email':data['email']}
            result = {'code': 0, 'msg': verify_result}
        else:
            verify_result = u'用户名密码错误'
            result = {'code': 1, 'msg': verify_result}
        #print result
        return result
    else:
        verify_result = {'code': 1, 'msg': u"不存在用户"}

    return verify_result

#verify_user('users', 'admin','yutian',user_field)

# 通过用户名查询
def query(tname,field,id=None):
    if not id :
        sql = "select %s from %s;" %(','.join(field),tname)
        cursor.execute(sql)
        query_result = cursor.fetchall()
        if query_result:
            user = [dict((k,row[i]) for i,k in enumerate(field))for row in query_result]
            result = {'code': 0, 'msg': user}
        else:
            msg = u'用户不存在'
            result = {'code': 1, 'msg': msg}
        return result
    else:
        sql = "select %s from %s where id='%s';" %(','.join(field),tname,id)
        cursor.execute(sql)
        query_result = cursor.fetchall()
        if query_result:
            user = {k: row[v] for row in query_result for v, k in enumerate(field)}
            result = {'code': 0, 'msg': user}
        else:
            msg = u'用户不存在'
            result = {'code': 1, 'msg': msg}
        return result
query('users',field)

def create(tname,field):
    sql = "insert into %s set %s;" %(tname,','.join(field))
    res = cursor.execute(sql)
    if  res:
        result = {'code':0,'msg':u'添加成功'}
        db.commit()
    else:
        result = {'code':1,'msg':u'添加失败'}
    return result

def query_all(tname,all_field):
    sql = 'select %s from %s;' %(','.join(all_field),tname)
    cursor.execute(sql)
    res = cursor.fetchall()

    if res:
        user = [dict((k,row[v]) for v,k in enumerate(all_field)) for row in res ]
        result = {'code':0, 'msg':user}
    else:
        result = {'code': 1, 'errmsg': 'data is null'}
    return result


def delete(tname,id):
    sql = "delete from %s where id='%s'" % (tname, id)
    cursor.execute(sql)

'''
fetchone()用法：
    cur.execute("select host,user,password from user where user='%s'" %acc)
    jilu = cur.fetchone()  ##此时 通过 jilu[0],jilu[1],jilu[2]可以依次访问host,user,password

fetchall()用法：
    cur.execute("select * from user")
    如果select本身取的时候有多条数据时：
    cursor.fetchone()：将只取最上面的第一条结果，返回单个元组如('id','title')，然后多次使用cursor.fetchone()，依次取得下一条结果，直到为空。
    cursor.fetchall() :将返回所有结果，返回二维元组，如(('id','title'),('id','title')),
    如果select本身取的时候只有一条数据时：
    cursor.fetchone()：将只返回一条结果，返回单个元组如('id','title')。
    cursor.fetchall() :也将返回所有结果，返回二维元组，如(('id','title'),),
'''