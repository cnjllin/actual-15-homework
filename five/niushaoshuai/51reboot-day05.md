## MVC名词解释：
- M: 模型，数据存储，对数据的增删改查。
- V：视图：前端页面展示，交由html，css,js代码控制。
- C：控制器： 控制端。flask框架。
## MVC 心法：
- 由外到内：V端html、css、js的数据通过get、post发送请求，C端（python）通过request.form.get()或request.args.get()接收V端的数据，格式化为需要的列表、字典、字符串，结合python语法存储到M端（存储端）。
- 由内到外：V端发送get请求想获取数据，C端python通过request.args.get()拿到get请求数据，python从M端读取数据如with open（）或pyhton的mysql模块的语法，由C端的python格式化为需要的列表、字典、字符串，暂时通过render_template和jinja2渲染到前端。
- 由外到内：
![image](http://i1.bvimg.com/608374/714971ec40a14636.jpg)
- 由内到外：
![image](http://i1.bvimg.com/608374/4cfad411f391d881.jpg)
* 如果需迭代，最好做成字典形式输出到html页面，以后写接口会涉及 *
## MVC适用场景
- V：
    - 密码类型：<input type="password" name="passwd">
    - 接收错误信息：<span style="color:red>{{ errmsg }}</span>    - 前端请求：<form action="/url/" method="POST">
- C:
    - 内部跳转：return redirect（'/url/'）
    - 优雅的错误信息：errmsg = "passwd is wrong"  ;return rend_template("index.html",errmag=errmsg)
- M: 
    - 存储数据的增，删，改，查。

## 代码赏析：
```
├── flask2login.zuoye.20180819.py  flask框架脚本
├── templates
│   ├── index.html                 首页
│   ├── login.html                 登陆页面
│   ├── reg.html                   注册页面
│   └── userlist.html              会员中心
├── userconf.py                    获取库文件功能模块
├── userinfo.py                    用户验证功能模块
└── user_message.db                库文件
```
```
* flask2login.zuoye.20180819.py *

#!/usr/bin/python 
# --*-- coding:UTF-8 --*--
from flask import Flask,request,render_template,redirect
import userinfo
test=Flask(__name__)

# 注册表单
# @app.route(‘/login’,methods=['GET','POST']) 如果访问/login  且方式是post或者get ，则执行下面的afterreg函数
@test.route('/reg/',methods=['GET','POST'])
def afterreg():
    if request.method == 'POST':
        username=request.form.get('name')
        user_pass1=request.form.get('pwd')
        user_pass2=request.form.get('pwd1')
	    if not userinfo.checkout_user_exist(username) and user_pass1 == user_pass2:
            f=open('user_message.db','a+')
            f.write("%s:%s \n" % (username,user_pass1))
            f.close()
            return render_template('reg.html',ok='Congratulations on your successful registration')
	    else:
	        return render_template('reg.html',ok='regist failed,agine')
    else:
        return render_template('reg.html')
# 会员中心
@test.route('/userlist/')
def userlist():
    f = open('user_message.db', 'r')
    message=f.readlines()
    f.close()
    return render_template('userlist.html',msg=message)

# 登陆表单
@test.route('/login/',methods=['GET','POST'])
def afterlogin():
    if  request.method == 'POST':
        user_name=request.form.get('name')
        user_pass=request.form.get('pwd')
        if userinfo.checkout_user_pass(user_name,user_pass):
            # redirect flask框架内部跳转，href是在html页面之间跳转。
            return redirect('/userlist/')
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
### 功能模块：
```
* userinfo.py：*

#!/usr/bin/python
# --*-- coding:UTF-8 --*--
import userconf

# 定义字典函数
# 在功能模块中建议不要出现全局参数，要都封装在模块内。否则会报一些奇葩的问题。ps:第一次定义字典的操作放在全局里面，当入口脚本调用时，新注册的用户无法立即登陆，要重启程序才可以。
def GetUser():
    f = open(userconf.USER_FILE, 'r')
    message = f.readlines()
    f.close()
    user_info=dict()
    for  line in message:
        mu = line.strip(' \n').split(':')[0]
        mp = line.strip(' \n').split(':')[1]
        user_info[mu]=mp
    return user_info
# 定义判断用户，密码验证函数
def checkout_user_pass(u, p):
    user=GetUser()
    if u in user.keys():
        if user[u] == p :
            return True

        else:
            return False
   
    else:
            return False
# 定义判断用户是否存在函数
def checkout_user_exist(u):
    user=GetUser()
    if  u in user.keys():
        return True
    else:
        return False
if __name__ == '__main__':
#    print checkout_user_pass('niushaoshuai1','123456')
#    print checkout_user_exist('niushaoshuai12')
    print checkout_user_pass('owen8','123')
```
```
* userconf.py *

#!/usr/bin/env python
# -*- coding: utf-8 -*-

USER_FILE = 'user_message.db'
```
### html页面文件
```
*index.html*

<html>
<head>
<meta charset="utf-8">
<title>首页</title>
</head>
<body>

<!-- href:a标签的属性，为对象增加超链接属性，超链接可以是相对url，也可以是绝对url -->
<!-- redirect flask框架内部跳转，href是在html页面之间跳转。 -->
<a href="login">老用户</a>
<a href="reg">新用户</a>
</body>
</html>
```
```
* login.html *

<html>
<head>
<meta charset="utf-8">
<title>登陆页面</title>
</head>
<body>

<!-- action匹配flask框架中的route部分，method则指定该表单的传参方式 -->
<form action="/login/" method="POST">
        <!-- 接受flask框架传过来的参数，如有打印出来，没有则为空 -->
        <!-- {%判断语句%} {{变量}} -->
        {% if error %}
        <span style='color:red'> {{error}} </span>
        {%endif%}
        用户名：
        <input type="text" name='name'> 
        密码：
        <!-- password 类型的输入本身就是加密的 -->
        <input type="password" name='pwd'>
        <input type="submit" value='提交'>
</form>
</body>
</html>

```
```
* reg.html *

<html>
<head>
<meta charset="utf-8">
<title>注册页面</title>
</head>
<body>

<form action="/reg/" method="POST">
        {% if error %}
            <span style='color:red'> {{error}} </span>
        {% elif ok %}
            <span style='color:green'> {{ok}} </span>
        {%endif%}
        用户名：
        <input type="text" name='name'> 
        密码：
        <input type="password" name='pwd'>
        重新输入密码：
        <input type="password" name='pwd1'>
        <input type="submit" value='提交'>
</form>
</body>
</html>
```

```
*userlist.html*

<html>
<head>
    <title>会员中心</title>
</head>
<table  border=1 >
    <thead>
        <tr>
                <th>NAME</th>
                <th>PASSWORD</th>
        </tr>
    </thead>
        <tbody>
            <!-- flask框架和html只交互一次，因此框架会一次性传输一个数据集合例如字典等参数，html页面要用到for循环遍历即可 -->
            {%  for m in msg %}
                        <tr>
                            <td>{{m.split(':')[0]}}</td>
                            <td>{{m.split(':')[1]}}</td>
                        </tr>
                {% endfor %}
    </tbody>
</table>
</html>
```

## 操作MySQL：
- 全局操作，永恒不变
```
In [2]: import MySQLdb as mysql

In [3]: db=mysql.connect(host='localhost',user='root',passwd='',db='51reboot',port=3306,charset='utf8')

In [4]: cur=db.cursor()      // 数据库实例化

```
- 实际操作，随遇而安
```

In [5]: sql='select * from user'

In [6]: cur.execute(sql)
Out[6]: 5L    //5行
In [7]: s=cur.fetchall()
In [8]: s
Out[8]: 
(
(1L, u'owen', u'test', 1L, 18L, 1532124124L, u'7931370@0@qq.com', 2L),
(2L, u'jim', u'test', 1L, 18L, 1522124124L, u'7831370@0@qq.com', 1L),
(3L, u'lily', u'test', 2L, 20L, 1552124124L, u'7631370@0@qq.com', 2L),
(4L, u'lilei', u'test', 1L, 21L, 1552324124L, u'7632370@0@qq.com', 1L),
(5L, u'duding', u'test', 1L, 25L, 1554324124L, u'7633370@0@qq.com', 1L)
)
 
* 结果是MySQL中每行作为一个元组，元组套元组的输出 即 元组嵌套 *

In [12]: cur.execute(sql)
Out[12]: 5L

In [13]: cur.fetchone()
Out[13]: (1L, u'owen', u'test', 1L, 18L, 1532124124L, u'7931370@0@qq.com', 2L)

* fetchone 只输出MySQL表里面的一行，把它存入一个元组 即 单元组 *

```
### 多字段查询操作：
```
多字段（>2）查询（用列表嵌套字典的方式输出）：
# 把要查询的字段放入列表中。
In [47]:Field=['id','username','password']
# 亮点 。
In [48]:sql='select %s from user' % (','.join(Field))
In [49]: cur.execute(sql)
In [50]:s=cur.fetchall()
#列表生成式套字典生成式
In [51]: users=[dict((k,row[i]) for i,k in enumerate(Field)) for row in s]  
Out[52]: 
[{'id': 1L, 'password': u'test', 'username': u'owen'},
 {'id': 2L, 'password': u'test', 'username': u'jim'},
 {'id': 3L, 'password': u'test', 'username': u'lily'},
 {'id': 4L, 'password': u'test', 'username': u'lilei'},
 {'id': 5L, 'password': u'test', 'username': u'duding'}]
# 最终以json格式显示。
In [55]: json.dumps({'code':0,'users':users})
Out[55]: '{"code": 0, "users": [{"username": "owen", "password": "test", "id": 1}, {"username": "jim", "password": "test", "id": 2}, {"username": "lily", "password": "test", "id": 3}, {"username": "lilei", "password": "test", "id": 4}, {"username": "duding", "password": "test", "id": 5}]}'

 
利用mysql索引的优势，查询（eg:(id,username)）双字段查询（用字典的方式输出）：
In [56]:  Field=['username','password']
In [57]: sql='select %s from user' % (','.join(Field))
In [58]: cur.execute(sql)
Out[58]: 5L
In [59]: s=cur.fetchall()
#或者直接执行：users=dict(s) ,即：fetchall后的结果本身就可以直接转换成字典
In [62]: users=dict((row[0],row[1]) for row in s)
In [63]: users
Out[63]: 
{u'duding': u'test',
 u'jim': u'test',
 u'lilei': u'test',
 u'lily': u'test',
 u'owen': u'test'}
json.dumps({'code':1 ,'users':users})
'{"code": 1, "users": {"lilei": "test", "jim": "test", "owen": "test", "lily": "test", "duding": "test"}}'
```
### 列表/字典生成式
```
字典生成式：
d = dict((key,value) for (key, value) in iterable)
列表生成式：
[x * x for x in range(1, 11)]
```

