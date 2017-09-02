## 代码结构规范
```
.
.
├── app.py       \\主程序
├── static       \\js相关目录
├── templates    \\html文件目录
│   ├── index.html
│   ├── login.html
│   ├── reg.html
│   ├── update.html
│   └── userlist.html
└── utils.py     \\功能模块
```

## 功能模块 utils.py
- 对主程序常用操作的封装：
    - mysql的增删改查
    - 登陆权限验证
    - 用户是否存在
    - 查询用户角色
    - 查询用户ID
- 使得主程序代码更加儒雅

```
#!/usr/bin/env python
# --*-- coding:UTF-8 --*--
import MySQLdb as mysql

# mysql实例化
conn = mysql.connect(host='localhost',user='root',passwd='',port=3306,db='51reboot',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

# 注意细节代码传参,虽然data是一个列表，但是不能直接用，需要每个元素用‘’包裹
def insert(table,field,*data):
    data2=[]
    for x in data:
       data2.append("'%s'" % x)
    sql = 'insert into %s (%s) values (%s)' % (table , ','.join(field) , ','.join(data2))
    cur.execute(sql)

# 注意细节，拼接单个变量时就没有那么多规矩，硬来。
def delete(table,uid):
    sql='delete  from user where id=%s' % uid
    cur.execute(sql)

#注意细节，这里的_value也是一个列表，方法见insert方法时的注意
def update(table,field,_value,uid):
    u=getone(table,field,uid)
    if u:
        u1=[]
        for v in _value:
            u1.append("'%s'" % v)
        u2=zip(field,u1)
        u3=['%s=%s' % (item[0],item[1]) for item in u2]
        sql='update %s set %s where id=%s' % (table,','.join(u3),uid)
        cur.execute(sql)     
        return getone(table,field,uid)

def list(table,field):
    sql = 'select * from %s' % table
    cur.execute(sql)
    res=cur.fetchall()
    if not res:
        result = {'code':1,'errmsg':'data is null'}
        return result
    else:
        users=[dict((k,row[i]) for i,k in enumerate(field)) for row in res]
        return users

def getone(table,field,uid):
    sql='select %s from %s where id=%s' % (','.join(field),table,uid)
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        result={'code':1,'errmsg':'data is null'}
        return result
    else:
       user=dict((k,res[i]) for i,k in enumerate(field))
       users=[]
       users.append(user)
       return users

# 注意细节，统一getone和list函数return的值都是[{},]样式，跟userlist.html保持一致。
def getrole(table,uname):
    sql = "select role from %s where u_name='%s'" % (table,uname)
    print sql
    cur.execute(sql)
    result=cur.fetchone()
    res=result[0]
    print res
    return res

def getid(table,uname):
    sql = "select id from %s where u_name='%s'" % (table,uname)
    cur.execute(sql)
    result=cur.fetchone()
    res=result[0]
    print res
    return res

def GetUser():
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
```

## 主程序部分 app.py
```
#!/usr/bin/python
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template,redirect
import utils
test=Flask(__name__)

#高频率变量提取，升级为全局变量。
filed=['id','u_name','password','sex','age','phone','email','role']
insert_filed=['u_name','password','sex','age','phone','email','role']

# 注册表单
@test.route('/reg/',methods=['GET','POST'])
def afterreg():
    if request.method == 'POST':
        username=request.form.get('name')
        user_pass1=request.form.get('pwd')
        user_pass2=request.form.get('pwd1')
        user_sex=request.form.get('sex')
        user_age=request.form.get('age')
        user_phone=request.form.get('phone')
        user_email=request.form.get('email')
        user_role=request.form.get('role')
        if not utils.checkout_user_exist(username) and user_pass1 == user_pass2:
            utils.insert('user',insert_filed,username,user_pass1,user_sex,user_age
,user_phone,user_email,user_role)
            return render_template('reg.html',ok='Congratulations on your successf
ul registration')
        else:
            return render_template('reg.html',ok='regist failed,agine')
    else:
        return render_template('reg.html')

# 会员中心-首页
@test.route('/userlist/')
def userlist():
    users=utils.list('user',filed)
    return render_template('userlist.html',msg=users)

# 会员中心-删除模块
@test.route('/delete/',methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        user_id=request.form.get('id')
    else:
        user_id=request.args.get('id')
    utils.delete('user',user_id)
    return redirect('/userlist/')

# 会员中心-更新模块
@test.route('/update/',methods=['GET','POST'])
def update():    
    if request.method == 'POST':
        user_id=request.form.get('id')
        user_name=request.form.get('name')
        user_pass=request.form.get('pwd')
        user_sex=request.form.get('sex')
        user_age=request.form.get('age')
        user_phone=request.form.get('phone')
        user_email=request.form.get('email')
        user_role=request.form.get('role')
        value=[user_id,user_name,user_pass,user_sex,user_age,user_phone,user_email
,user_role]
        user=utils.update('user',filed,value,user_id) 
        return render_template('update.html',msg=user,error='update ok')

    else:
        user_id=request.args.get('id')
        user=utils.getone('user',filed,user_id)
        return render_template('update.html',msg=user)

# 登陆模块
@test.route('/login/',methods=['GET','POST'])
def afterlogin():
    if  request.method == 'POST':
        user_name=request.form.get('name')
        user_pass=request.form.get('pwd')
        print user_name
        user_id=utils.getid('user',user_name) 
        user_role=utils.getrole('user',user_name)
        if utils.checkout_user_pass(user_name,user_pass):
            # 增加用户身份验证功能
            if user_role == 0:
                return redirect('/userlist/')
            else:
                users=utils.getone('user',filed,user_id)    
                print users
                return render_template('userlist.html',msg=users)
        else:
            return render_template('login.html',error='username or password is error')
    else:
        
        return render_template('login.html')

# 首页
@test.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    test.run(host='0.0.0.0',port=5678,debug=True)
```

## SQL 拼接

- 用法: % 前面用‘’包裹，除了%s 其他都是字符串，% 后面是变量部分用（）包裹
- 语法: sql='sting1 %s sting2 %s stringn from %s' % (x,y,z)

- SQL 语句中%s 与 变量一对一时：
    - 用法：% 前用单引号‘’包裹即可
    - 实例：sql='delete  from %s where id=%s' % (table,uid)

- SQL 语句中%s 与 变量一对多时：
    - 变量值需要用‘’包裹时：
        - 用法：变量一般为列表或者字典类型，需要遍历每个元素值，保证都有引号包裹
        - 实例：
        ![image](http://i4.bvimg.com/608374/28696029bd1e32c7.png)
    - 变量值不需要用‘’包裹时：
        - 用法：'%s' % ','.join(field)
        - 实例：
        ![Markdown](http://i4.bvimg.com/608374/392641cd1b776c4a.png)
    

    
    
    
    
    
    
    
    

