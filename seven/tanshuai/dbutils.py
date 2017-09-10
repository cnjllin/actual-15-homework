#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Nick on 2017/8/21日14点51分

import MySQLdb as mysql

"""创建一个数据库操作函数，功能定义如下：
1. 函数接收三个参数：sql，args，fetch
2. 参数说明：
    sql：接收前端拼接sql语句
    args：接收一个元组，default：空元组
    fetch：
        默认True，即执行：查询指令
        赋值False时，即执行：添加/更新/删除指令
"""
def execute_sql(sql, args=(), fetch=True):
    conn = None
    count = 0
    rt_list = []
    try:
        # 创建一个mysql连接
        conn = mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='reboot15', charset='utf8')
        # 获取游标
        cur = conn.cursor()
        if fetch == 'fetchone':
            # 执行查询指令
            count = cur.execute(sql, args)
            rt_list = cur.fetchone()
        elif fetch:
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

if __name__ == "__main__":
    # 查询所有用户
    # sql = "select * from user"
    # 增加一个用户
    sql = "insert into user(username,password,sex,age,phone,email,role) values(%s,%s,%s,%s,%s,%s,%s)"
    args = ('谭帅02','123456',1,27,'18512341234','185@185.com',1)
    # 删除一个用户
    # sql = 'delete from user where id=%s'
    # args = (1,)
    # 更新一个用户
    # sql = "update user set username=%s,password=%s,sex=%s,age=%s,phone=%s,email=%s,role=%s where id=%s"
    # args = ('谭帥03','123456',1,27,'18512341234','185@185.com',1,15)
    count, rt_list = execute_sql(sql=sql, args=args, fetch=False)
    # count, rt_list = execute_sql(sql=sql)
    print count, rt_list