# -*- coding:utf-8 -*-
import sys
reload(sys)
print sys.getdefaultencoding()
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
import MySQLdb as mdb


def exec_sql(sql) :
    #conn=mdb.connect(host="127.0.0.1",user="root",passwd="Lqm@135246",db="mydb1",port=3306,charset='utf8',cursorclass = mdb.cursors.DictCursor)
    #cur=conn.cursor()
    #上面两行等价于下面两行,返回的单条结果为键值对的字典
    conn=mdb.connect(host="127.0.0.1",user="root",passwd="Lqm@135246",db="mydb1",port=3306,charset='utf8')
    cur = conn.cursor(cursorclass = mdb.cursors.DictCursor)
    try:
        print "exec sql: %s" % sql
        res = cur.execute(sql)  #条数
        sqlres = cur.fetchall() #结果
        conn.commit()
        print "count: %s , result: %s" % (res,sqlres)  #为什么这条会输出两次 
        return sqlres
    except mdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        conn.rollback()
        return "Mysql Error %d: %s" % (e.args[0], e.args[1])
    finally:
        cur.close()
        conn.close()

#查询所有用户，返回元组
def chaxun():
    sql = "select * from user_info;"
    res = exec_sql(sql)
    return res

#按照uid查询
def cha_uid(uid):
    sql = "select * from user_info where uid = %s;" % uid
    res = exec_sql(sql)
    if len(res) > 0 :
        res = exec_sql(sql)[0]
        return res

#注册函数
def insert(users) :
    user_infos = chaxun()
    usernames = []
    usernames = [ user_info['username'] for user_info in user_infos ]
    if users.get('username') in usernames :
        #print "用户名%s已经存在" % users.get('username')
        res = False
    else :
        values = str(tuple(users.values())).replace('u\'','\'').decode("unicode-escape") 
        sql = "insert into user_info (%s) values %s;" % ( ",".join(users.keys()), values)
        #print sql
        username = users.get('username')
        sqlres = exec_sql(sql)
        #print  "用户名%s注册成功" %  users.get('username')
        res = True
    return res

#删除用户
def delete(users) :
    if isinstance(users,dict) :
        user_info = select(users)
        uid = user_info['uid']
    else :
        uid = users
    sql = "delete from user_info where uid = %s;" % uid
    sqlres = exec_sql(sql)
    sql1 = "ALTER TABLE user_info AUTO_INCREMENT = 1; "
    sql1res = exec_sql(sql1)
    return sqlres

#根据用户名查询数据库用户信心，返回元组
def select(users) :
    userinfos = chaxun()
    for index,user_info in enumerate(userinfos) :
        if users.get('username') == user_info['username'] :
            res = userinfos[index]
            res = user_info
            break
        else :
            pass
    else :
        #res = "用户名不存在" % users.get('username')
        res = False
    return res
    
#更新用户信息
def update(users) :
    print str(type(users))
    #if str(type(users)) == "<type 'dict'>" :
    if isinstance(users,dict) :
        user_info = select(users)
        uid = user_info['uid']
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
    sqlres = exec_sql(sql)
    print sqlres
    return sqlres
def insert_article(articles):
    sql = "insert into articles (%s) values (%s);" % (",".join(articles.keys()),",".join([ "'%s'" % mdb.escape_string(str(v)) for v in articles.values() ] )  )  #mdb.escape_string()参数必须字符串
    sql = "insert into articles (%s) values (%s);" % (",".join(articles.keys()),",".join([ "'%s'" % str(v).replace("'",'\\"') for v in articles.values() ] )  )  #replace()是字符串方法
    sql = "insert into articles (%s) values (%s);" % (",".join(articles.keys()),",".join([ '"%s"' % str(v).replace("\"","\\'") for v in articles.values() ] ) ) #replace()是字符串方法 
    sqlres = exec_sql(sql)
    return sqlres
        
def search_art(search_texts):
    #sql = "select * from articles where title like '%%%s%%'; " % mdb.escape_string(search_texts.get('title') )
    sql = "select a.*,b.username from articles a left join user_info b on a.author_id = b.uid where title like '%%%s%%' ;" % mdb.escape_string(search_texts.get('title') )
    print sql
    sqlres = exec_sql(sql)
    print type(sqlres),sqlres
    return sqlres

#cha_uid(110004)
#cha_uid(190000)
#print delete(1111121)    
#users ={'username':'100000','passwd':'123456','age':100,'sex':'2','phone':'66666','email':'lqm@123.com','role':0}
#print "1212121",insert(users)
#users ={'username':u'李白','passwd':'123456','age':10000,'sex':u'男','phone':'66666','email':'lqm@123.com','role':0}
#print update(users)
#print cha_uid(1)    
#print cha_uid(2)    
#print chaxun()    
#users ={'username':u'刘清明','passwd':'123456','age':10,'sex':u'男','phone':'66666','email':'lqm@123.com','role':0}
#insert(users)
