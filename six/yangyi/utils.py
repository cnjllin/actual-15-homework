# Author: tailorYang
import mysql.connector as mysql

class DB():
    def __init__(self):
        self.__user = 'root'
        self.__password = 'yangyi'
        self.__database = 'reboot15'
        self.__charset = 'utf8'
        self.table = None
        try:
            self.conn = mysql.connect(
                user=self.__user,
                password=self.__password,
                database=self.__database,
                charset=self.__charset
            )
        except Exception as e:
            print("MySQL ERROR %s" % e)
        self.cursor = self.conn.cursor()

    #查询多条结果
    def fetch_all(self,sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            result = "Mysql Error:%s\nSQL:%s" %(e,sql)
        return result

    # 查询一条结果
    def fetch_one(self,sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
        except Exception as e:
            result = "Mysql Error:%s\nSQL:%s" %(e,sql)
        return result

    # updat OR insert

    def commit(self,sql):
        try:
            self.cursor.execute(sql)
            result =self.cursor.rowcount
            self.conn.commit()
        except Exception as e:
            result = "Mysql Error:%s\nSQL:%s" % (e, sql)
        return result

    def close(self):
        if (self.conn):
            try:
                if(type(self.cursor)=='object'):
                    self.cursor.close()
                if(type(self.conn)=='object'):
                    self.conn.close()
            except Exception as e:
                return "close database exception, %s,%s,%s" % (e, type(self.cursor), type(self.conn))



