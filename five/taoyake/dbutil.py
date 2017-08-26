#/usr/bin/python
# -*- coding: utf-8 -*-

#导入MySQLdb模块
import MySQLdb as mysql

def execute_sql(sql, args=(), fetch=True):
    conn = None
    count = 0
    rt_list = []
    try:
        # 创建一个mysql连接
        conn = mysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='taoyake', charset='utf8')
        # 获取游标
        cur = conn.cursor()
        if fetch:
            # 执行查询指令
            count = cur.execute(sql, args)
            rt_list = cur.fetchall()
        else:
            # 执行增/删/改指令
            count = cur.execute(sql, args)
            conn.commit()
    except Exception as e:
        print 'Error %d: %s' % (e.args[0], e.args[1])
    finally:
        if conn:
            conn.close()
    return count, rt_list
