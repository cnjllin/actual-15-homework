# Author: tailorYang
import mysql.connector as mysql
import config,traceback,utils

try:
    conn = mysql.connect(**config.config)
    cursor = conn.cursor()
except :
    utils.writelog('db').error('"Error: %s"'% (traceback.format_exc()))

def select(table,*fields,**data):
    data = ' and '.join({'%s="%s"' % (k, v) for k, v in data.items()})
    fields = ','.join(fields)
    if data and fields :
        sql = 'SELECT {} FROM {} WHERE {};'.format(fields,table,data)
    elif not data and fields:
        sql = 'SELECT {} FROM {};'.format(fields,table)
    elif not fields and data:
        sql = 'SELECT * FROM {} WHERE {};'.format(table,data)
    else:
        sql = 'SELECT * FROM {};'.format(table)
    try :
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except:
        utils.writelog('db').error('"Exec: %s,"Error: %s"'% (sql,traceback.format_exc()))


def update(table,condition,id):
    sql = 'UPDATE {} SET {} WHERE id = {};'.format(table,','.join(condition),id)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        utils.writelog('db').error('"Exec: %s,"Error: %s"' % (sql, traceback.format_exc()))
    return cursor.rowcount
def delete(table,id):
    sql = 'DELETE FROM {} WHERE id = {};'.format(table,id)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        utils.writelog('db').error('"Exec: %s,"Error: %s"' % (sql, traceback.format_exc()))
    return cursor.rowcount

def add(table,data):
    sql = 'INSERT INTO {} ({}) VALUES({});'.format(table,','.join(data.keys()),','.join(['"%s"'%k for k in data.values()]))
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        utils.writelog('db').error('"Exec: %s,"Error: %s"' % (sql, traceback.format_exc()))
    return cursor.rowcount

