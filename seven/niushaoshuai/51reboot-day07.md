## 代码优化
### 工具函数 utils.py
```
#!/usr/bin/env python
# --*-- coding:UTF-8 --*--
import MySQLdb as mysql


conn = mysql.connect(host='localhost',user='root',passwd='',port=3306,db='51reboot',charset='utf8')
conn.autocommit(True)
cur = conn.cursor()

def insert(table,field,data):
    sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
    res = cur.execute(sql)
    if res:
        result = {'code':0,'msg':'insert ok'}
    else:
        result = {'code':1,'msg':'insert fail'}
    return result

def delete(table,uid):
    sql='delete  from user where id=%s' % uid
    cur.execute(sql)

def update(table,field,data):
    condition = ["%s='%s'"%(k,data[k]) for k in data]
    sql = "update %s set %s where id='%s';"%(table,','.join(condition),data['id'])
    res=cur.execute(sql)
    if  res:
        result = {'code':0,'msg':'update ok'}
    else:
       result = {'code':1,'msg':'update fail'}
    return result 

def list(table,field):
    sql = 'select * from %s' % table
    cur.execute(sql)
    res=cur.fetchall()
    if not res:
        result = {'code':1,'errmsg':'data is null'}
    else:
        users=[dict((k,row[i]) for i,k in enumerate(field)) for row in res]
        result = {'code':0,'msg':users}
        return result

def getone(table,field,uid):
    sql='select %s from %s where id=%s' % (','.join(field),table,uid)
    cur.execute(sql)
    res=cur.fetchone()
    if not res:
        result={'code':1,'errmsg':'data is null'}
    else:
       user=[dict((k,res[i]) for i,k in enumerate(field))]
       result = {'code':0,'msg':user}
    return result

def getrole(table,uname):
    if checkout_user_exist(uname):
        sql = "select role from %s where u_name='%s'" % (table,uname)
        cur.execute(sql)
        result=cur.fetchone()
        res=result[0]
        return res

def getid(table,uname):
    if checkout_user_exist(uname):
        sql = "select id from %s where u_name='%s'" % (table,uname)
        cur.execute(sql)
        result=cur.fetchone()
        res=result[0]
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
### 相对day06改进之处
- 改进一：
![Markdown](http://i4.bvimg.com/608374/f7d693a97d5511a8.png)
- 改进二：
![Markdown](http://i4.bvimg.com/608374/0f986043fc7cea9f.png)
- 改进三：
![Markdown](http://i4.bvimg.com/608374/e401667f014a7e5d.png)
-改进四：
![Markdown](http://i4.bvimg.com/608374/234f9625d5c91d05.png)
- 改进五：
![Markdown](http://i2.bvimg.com/608374/9164a0c8aeb468a3.png)


## 主程序 flask2login.zuoye.20170830v2.py
```
#!/usr/bin/python
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template,redirect,session
import utils
import json
test=Flask(__name__)
test.secret_key='sdfsfklsdlflfd'

filed=['id','u_name','password','sex','age','phone','email','role']
insert_filed=['u_name','password','sex','age','phone','email','role']

# 注册表单
@test.route('/reg/',methods=['GET','POST'])
def afterreg():
    if request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        if not utils.checkout_user_exist(user_data['u_name']) and user_data['password'] == user_data['password1']:
            res=utils.insert('user',insert_filed,user_data)
            if res['code'] == 0:
                return redirect("/login/")
        else:
            return render_template('reg.html',ok='regist failed,agine')
    else:
        return render_template('reg.html')

# 会员中心-首页
@test.route('/userlist/')
def userlist():
    if not session:
        return redirect("/login")
    else:
        users=utils.list('user',filed)
        users1=json.dumps({'code':0,'users':users})
        if users['code'] == 0:
            return render_template('userlist.html',msg=users['msg'])

# 个人用户-首页
@test.route('/userlist1/')
def userlist1():
    if not session:
        return redirect("/login")
    else:
        user_id=session['id']
        users=utils.getone('user',filed,user_id)
#        users1=json.dumps({'code':0,'users':users})
        if users['code'] == 0:
            return render_template('userlist.html',msg=users['msg'],user=users)

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
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user=utils.update('user',filed,user_data) 
        if user['code']==0:
              return redirect("/userlist/")
        else:
             return render_template('update.html',error=user['msg'])

    else:
        user_id=request.args.get('id')
        user=utils.getone('user',filed,user_id)
        if user['code'] == 0:
            return render_template('update.html',msg=user['msg'])

# 登陆模块
@test.route('/login/',methods=['GET','POST'])
def afterlogin():
    if  request.method == 'POST':
        user_info_dict=dict(request.form)
        user_data={ k:v[0] for k,v in user_info_dict.items() }
        user_id=utils.getid('user',user_data['u_name']) 
        user_role=utils.getrole('user',user_data['u_name'])
        if utils.checkout_user_pass(user_data['u_name'],user_data['password']):
            session['username']=user_data['u_name']
            session['id']=user_id
            session['role']=user_role
            if user_role == 0:
                return redirect('/userlist/')
            else:
                return redirect('/userlist1/')
        else:
            return render_template('login.html',error='username or password is error')
    else:
        
        return render_template('login.html')


# 登出
@test.route('/logout/')
def logout():
    session.clear()
    return redirect("/login")


# 首页
@test.route('/')
def index():
    if not session:
        return redirect("/login")
    else:
        return render_template('index.html')
if __name__ == '__main__':
    test.run(host='0.0.0.0',port=5678,debug=True)

```
### 相对day06改进之处
- 改进一：
![Markdown](http://i2.bvimg.com/608374/363850e10da8202d.png)
- 改进二：
![Markdown](http://i2.bvimg.com/608374/f0f0a4f6f8f3aa97.png)
- 改进三：
![Markdown](http://i2.bvimg.com/608374/4cc1e4a60f71a6c6.png)

## session 介绍
### session可以理解为一个全局大字典，它允许你在不同请求间存储特定用户的信息。
- 全局的变量
- 字典类型
- 可以通过get获取指定值
- cookies基础上实现，可读不可写
- 用户只能通过session获取到个人信息
- 前后端通吃

#### 使用方法：
```
from flask import sesssion
test.secret_key='sdfsfklsdlflfd'
session['name']='reboot'
print session['name']
```

### cur.execute() 
- 执行成功返回影响到的行数
- 执行失败返回none类型

## JQUERY 使用方法：
- 导入：<head> <script src="/static/js/jquery-2.1.1.js"></script> </head>
- 根据id获取数据并渲染更新表单：
```
<script>
var id = {{ uid }}    //获取到用户id
var url = "/userinfo/?id="+id //相当于html中的action
console.log(url)       //ajax渲染url，直接在浏览器中看log
$.getJSON(url,function(data)
{console.log(data)
    $("#username").val(data['username'])
    $("#password").val(data['password'])
}
)
</scritpt>
```
- 修改html内容，增加'id= '字段

