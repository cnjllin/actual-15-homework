# -*- coding:utf-8 -*-
import MySQLdb as mdb
db=mdb.connect(host="127.0.0.1",user="root",passwd="Lqm@135246",db="mydb1",port=3306,charset='utf8')
cur = db.cursor()

#查询所有用户，返回元组
def chaxun():
    sql = "select * from user_info;"
    res = cur.execute(sql)
    res=cur.fetchall()
    return res

#按照uid查询
def cha_uid(uid):
    sql = "select * from user_info where uid = %s;" % uid
    res = cur.execute(sql)
    res=cur.fetchone()
    return res

#注册函数
def insert(users) :
    user_infos = chaxun()
    usernames = []
    usernames = [ user_info[1] for user_info in user_infos ]
    if users.get('username') in usernames :
        #res = "用户名%s已经存在" % users.get('username')
        res = False
    else :
        values = str(tuple(users.values())).replace('u\'','\'').decode("unicode-escape") 
        sql = "insert into user_info (%s) values %s;" % ( ",".join(users.keys()), values)
        #print sql
        username = users.get('username')
        sqlres = cur.execute(sql)
        db.commit()
        #res =  "用户名%s注册成功" %  username   #users.get('username')
        res = True
    print res
    return res

#删除用户
def delete(users) :
    if isinstance(users,dict) :
        user_info = select(users)
        uid = user_info[0]
    else :
        uid = users
    sql = "delete from user_info where uid = %s;" % uid
    sqlres = cur.execute(sql)
    db.commit()

def select(users) :
    userinfos = chaxun()
    for index,user_info in enumerate(userinfos) :
        if users.get('username') == user_info[1] :
            res = userinfos[index]
            break
        else :
            pass
    else :
        #res = "用户名不存在" % users.get('username')
        res = False
    return res
    

def update(users) :
    print str(type(users))
    #if str(type(users)) == "<type 'dict'>" :
    if isinstance(users,dict) :
        user_info = select(users)
        uid = user_info[0]
        print user_info, uid,'12313131'
    else :
        uid = users
        print  uid,'asdasd'

    passwd = users.get('passwd')
    age = users.get('age')
    sex = users.get('sex')
    print sex
    phone = users.get('phone')
    email = users.get('email')
    role  = users.get('role')
    sql = "update user_info set passwd = '%s',age = '%s',sex = '%s', phone = '%s',email = '%s',role = '%s' where uid = '%s'; " % (passwd,age,sex,phone,email,role,uid) 
    print sql
    sqlres = cur.execute(sql)
    db.commit()
         
        
    
    
#users ={'username':u'刘清明','passwd':'123456','age':10,'sex':u'男','phone':'66666','email':'lqm@123.com','role':0}
#insert(users)
#users ={'username':u'刘清明','passwd':'123456','age':18,'sex':u'男','phone':'66666','email':'lqm@123.com','role':0}
#update(users)
#delete(users)
#print chaxun()