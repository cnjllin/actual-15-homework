import MySQLdb as mysql
db=mysql.connect(host="192.168.50.160",user="root",passwd="zhaoxf513",db="reboot15",port=3306,charset='utf8')
cur=db.cursor()
fields = ['id','username', 'password', 'role']
sql_list = "select * from user;"
cur.execute(sql_list)
list = cur.fetchall()
col_list = ['id', 'username', 'password', 'role']
user_list = [dict((k, v[i]) for i, k in enumerate(col_list)) for v in list]
print user_list
for i in user_list:
    print i['username'],i['password'],i['role'],i['id']
# user_dict = dict((k,list[i]) for i,k in enumerate(fields))
# user_list = dict((k,row[i]) for i,k in enumerate(fields))for row in user_dict
# userdict={}
# namelist=[]
# valuelist=[]
# user_info = {}
# error_mes = {'code':'0','msg':''}
# d = {'name':'wd','age':18,'sex':'nan'}
# c = {v:k for k,v in d.items()}
# user = [1,'wd','1123','sa']
# info = ['id','name','password','role']
# c = {}
# for k,v in enumerate(info):
#      c[v] = user[k]
# print c

# print user_dict
# for i in list:
#     # user_info['id'] = int(i[0])
#     user_info['username'] = ''.join(map(lambda x: "%c" % ord(x), i[1]))
#     user_info['password'] = ''.join(map(lambda x: "%c" % ord(x), i[2]))
#     user_info['sex'] = i[3]
#     user_info['age'] = i[4]
#     user_info['phone'] = i[5]
#     user_info['email'] = ''.join(map(lambda x: "%c" % ord(x), i[6]))
#     user_info['role'] = i[7]
#     for k in user_info:
#         namelist.append(k)
#         valuelist.append(user_info[k])
#         for a in range(0, len(valuelist)):
#             valuelist[a] = str(valuelist[a])
# print namelist,valuelist
# print user_info
# it =  ",".join(i for i in namelist)
# va =  ",".join(v for v in valuelist)
# print it,va
#
# print 'insert into user(%s) values(%s);'%(it,va)
#
# insert into user(username,age,sex,phone,role,password,email) values('da',19,0,18210,0,'123456','da@reboot.com');



# print "".join([ 'insert into user(%s) values ();'% (i,v) for k,v in user_info.items()])
# for a in userdict:
#     namelist.append(a)
# if name in namelist:
#     if passwd == userdict[user]:
#         error_mes['code'] = 1
#     else:
#         error_mes['code'] = 2
#         error_mes['msg'] = 'your password is not right!'
# else:
#     error_mes['code'] = 0
#     error_mes['msg'] = 'your username is not exist!'
# print error_mes

# print b,c

