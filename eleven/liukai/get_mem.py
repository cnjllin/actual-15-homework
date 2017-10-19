#! /usr/bin/env python
# _*_coding:utf-8_*_
import psutil
import time
import MySQLdb
import config
db=MySQLdb.connect(host=config.host,
                   user=config.user,
                   passwd=config.passwd,
                   db=config.db,
                   port=config.port,
                   charset=config.charset)
cur=db.cursor()
db.autocommit(True)



while True:
    memfree=psutil.virtual_memory().free/1024/1024
    sql='insert into mem values(%s,%s)'%(memfree,int(time.time()))
    print sql
    cur.execute(sql)
    time.sleep(1)

