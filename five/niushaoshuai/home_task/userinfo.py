#!/usr/bin/python
# --*-- coding:UTF-8 --*--
import userconf
import MySQLdb as mysql


def GetUser():
    db = mysql.connect(host='localhost', user='root', passwd='', port=3306, db='51reboot', charset='utf8')
    cur = db.cursor()
    filed=['u_name','password']
    sql='select %s  from user' %  (','.join(filed))
    cur.execute(sql)
    s=cur.fetchall()
    user_info=dict((row[0],row[1])  for row in s)
    return user_info


def checkout_user_pass(u, p):
    user = GetUser()
    if u in user.keys():
        if user[u] == p:
            return True

        else:
            return False

    else:
        return False


def checkout_user_exist(u):
    user = GetUser()
    if u in user.keys():
        return True
    else:
        return False


if __name__ == '__main__':
    #    print checkout_user_pass('niushaoshuai1','123456')
    #    print checkout_user_exist('niushaoshuai12')
    print checkout_user_pass('owen8', '123')
