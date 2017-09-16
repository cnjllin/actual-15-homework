# Author: tailorYang
import mysql.connector as mysql
import config

try:
    conn = mysql.connect(**config.config)
    cursor = conn.cursor()
except Exception as e:
    error = e

def select_one(table,fields='*',**data):
    if data.get('id'):
        sql = 'SELECT {} FROM {} WHERE id = {};'.format(','.join(fields),table,data['id'])
    elif len(data) > 0:
        data = ' and '.join({'%s="%s"'%(k,v) for k,v in data.items()})
        sql = 'SELECT {} FROM {} WHERE {};'.format(','.join(fields),table,data)
    else:
        sql = 'SELECT {} FROM {} ;'.format(','.join(fields),table)
    try :
        cursor.execute(sql)
        res = cursor.fetchall()
        result = [dict((v,row[k])  for k,v in enumerate(fields)) for row in res]
        result = {'code': 1 ,'result':result}
    except Exception as e:
        result = {'code': 0 ,'result':'{}+{}'.format(e,sql)}
    return result

def update(table,condition,id):
    sql = 'UPDATE {} SET {} WHERE id = {};'.format(table,','.join(condition),id)
    cursor.execute(sql)
    conn.commit()


def delete(table,id):
    sql = 'DELETE FROM {} WHERE id = {};'.format(table,id)
    cursor.execute(sql)
    conn.commit()

def add(table,data):
    sql = 'INSERT INTO {} ({}) VALUES({});'.format(table,','.join(data.keys()),','.join(['"%s"'%k for k in data.values()]))
    print(sql)
    cursor.execute(sql)
    conn.commit()
    return cursor.rowcount

