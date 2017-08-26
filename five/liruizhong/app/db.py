#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb

class DB(object):
    def __init__(self):
        self.db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="reboot",
        passwd="reboot@123",
        db="reboot15",
        charset="utf8"
    )

    def select(self,sql):
        cursor = (self.db).cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except:
            print "数据异常!!"
        finally:
            (self.db).close()
        return results

    def insert(self,sql):
        cursor = (self.db).cursor()
        try:
            cursor.execute(sql)
            (self.db).commit()
            (self.db).close()
            return  True
        except:
            (self.db).rollback()
            (self.db).close()
            return  False

    def update(self,sql):
        cursor = (self.db).cursor()
        try:
            cursor.execute(sql)
            (self.db).commit()
            (self.db).close()
            return  True
        except:
            (self.db).rollback()
            (self.db).close()
            return  False

    def delete(self,sql):
        cursor = (self.db).cursor()
        try:
            cursor.execute(sql)
            (self.db).commit()
            (self.db).close()
            return  True
        except:
            (self.db).rollback()
            (self.db).close()
            return  False
