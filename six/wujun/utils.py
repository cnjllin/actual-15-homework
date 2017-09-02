#coding:utf8
import MySQLdb
db=MySQLdb.connect(host="192.168.1.8",user="root",passwd="wujun",db="reboot15",port=3306,charset="utf8")
cur=db.cursor()
db.autocommit(True)



# 增
def insert(User,data):
     user_list=[]
     values=[]
     for k,v in data.items():
         user_list.append(k)
         values.append("'%s'"%v)
     sql="insert into %s (%s) values(%s)"%(User,','.join(user_list),','.join(values))
     print sql
     cur.execute(sql)
     result ={'code':1,'errmsg':'ok'}
     return result


# 删
def delete(User,uid):
   sql="delete from %s where id =%s"%(User,uid)
   print sql
   cur.execute(sql)
   result ={'code':1,'errmsg':'ok'}
   return result

# 改
def update(User,filed,data):
    conditions=['%s="%s"'%(k,data[k])for k in data]
    sql="update %s set %s where id=%s"%(User,','.join(conditions),data['id'])
    print sql
    cur.execute(sql)
    result={'code':1,'errmsg':'ok'} 
    return result

# 查all
def list(User,user_list):
    sql="select * from %s"%User
    print sql
    cur.execute(sql)
    res=cur.fetchall()
    user=[{k:row[i] for i,k in enumerate(user_list)}for row in res]
    return user

# 查单个用户
def get_one(User,user_list,uid):
   sql="select * from %s where id =%s"%(User,uid)
   cur.execute(sql)
   res=cur.fetchone()
   user={k:res[i] for i,k in enumerate(user_list)}
   return user

# 根据username查
def get_name(User,user_list,username):
   sql="select * from %s where username='%s'"%(User,username)
   cur.execute(sql)
   res=cur.fetchone()
   return res





