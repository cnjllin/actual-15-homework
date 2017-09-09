# Author: tailorYang
# Author: tailorYang
import mysql.connector as mysql

conn = mysql.connect(user='root',passwd='yangyi',host='localhost',db='reboot15',charset='utf8')
cursor = conn.cursor()

def get_one(table,fields,data):
    if  'id' not in data.keys():
        sql = 'select * from {} where  name = "{}"'.format(table,data['name'])
    else:
        sql = "select * from {} where id = {}".format(table,data['id'])
    try:
        cursor.execute(sql)
        user = cursor.fetchone()
        result = {v:user[k] for k,v in enumerate(fields)}
    except Exception as e:
        result = "Mysql Error:%s\nSQL:%s" % (e, sql)
    return result

def list(table,fields,id=None):
    if not id:
        sql = 'select * from {}'.format(table)
        try:
            cursor.execute(sql)
            user = cursor.fetchall()
            result = [dict((v, row[k]) for k, v in enumerate(fields)) for row in user]
        except Exception as e:
            result = "Mysql Error:%s\nSQL:%s" % (e, sql)
    else:
        sql = 'select * from {} Where id = {}'.format(table,id)
        try:
            cursor.execute(sql)
            user = cursor.fetchone()
            result = {v:user[k] for k,v in enumerate(fields)}
        except Exception as e:
            result = "Mysql Error:%s\nSQL:%s" % (e, sql)
    return result

def update(table,args,id):
    sql = "update %s set %s where id='%s'"%(table,','.join(args),id)
    cursor.execute(sql)
    conn.commit()

def delete(table,id):
    sql = "delete from %s where id='%s'"%(table,id)
    cursor.execute(sql)
    conn.commit()

def add(table,args):
    try:
        sql = 'insert into %s set %s'%(table,','.join(args))
        cursor.execute(sql)
        conn.commit()
    except  Exception as e:
        return "Exec: {},Error: {}".format(sql, e)

