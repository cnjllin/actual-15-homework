### Mysql安装配置
1. 安装Mysql
```bash
wget http://repo.mysql.com/mysql57-community-release-el7-9.noarch.rpm
rpm -ivh mysql57-community-release-el7-9.noarch.rpm
yum install mysql-community-server
```
2. 配置文件设置默认编码utf-8
```bash
vim /etc/my.cnf
[client]
default-character-set = utf8

[mysqld]
default-storage-engine = INNODB
character-set-server = utf8
collation-server = utf8_general_ci
systemctl restart mysqld.service

mysql> show variables like '%char%';
+--------------------------------------+----------------------------+
| Variable_name                        | Value                      |
+--------------------------------------+----------------------------+
| character_set_client                 | utf8                       |
| character_set_connection             | utf8                       |
| character_set_database               | utf8                       |
| character_set_filesystem             | binary                     |
| character_set_results                | utf8                       |
| character_set_server                 | utf8                       |
| character_set_system                 | utf8                       |
| character_sets_dir                   | /usr/share/mysql/charsets/ |
| validate_password_special_char_count | 1                          |
+--------------------------------------+----------------------------+

```
3. 创建数据库mydb1,在mydb1创建表user_info
```mysql
mysql -uroot -p
mysql> CREATE DATABASE mydb1 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
mysql> show databases;
create table user_info(
    uid int not null auto_increment,
    username varchar(20) not null,
    passwd varchar(20) not null,
    age int,
    sex varchar(4) ,
    phone varchar(20) not null,
    email varchar(40),
    role int not null,
    primary key(username),
    index(uid)
            );
mysql> SHOW TABLES;
mysql> desc user_info;
mysql> insert into user_info (username,passwd,age,phone,email,role) values ('lqm','123456',1,'2312312312','lqm@123.com',0);
```
4. 在age字段后添加sex字段，并设置为非空
```mysql
alter table user_info add sex varchar(10) after age;
update user_info set sex = '男' ;
alter table user_info modify sex varchar(10) not Null;
```
### 作业
1. 安装virtualenv
```bash
pip install virtualenv
find / -name virtualenv
ln -s  $(find / -name virtualenv) /usr/bin/virtualenv
```
2. 创建一个虚拟环境
```bash
mkdir liuqingming && cd liuqingming
virtualenv flask
```
3. 创建目录
```bash
mkdir app
mkdir app/static     #存放静态文件
mkdir app/templates  #存放模板文件
mkdir tmp
```
4. 安装模块
```bash
[root@localhost liuqingming]#flask/bin/pip install flask
[root@localhost liuqingming]# flask/bin/pip install MySQL-python
Collecting MySQL-python
Installing collected packages: MySQL-python
Successfully installed MySQL-python-1.2.5
```
5. 创建一个简单的初始化脚本app/__init__.py
```python
from flask import Flask

app = Flask(__name__)
from app import views
```
6. 编写第一个视图函数(文件 app/views.py )
```python
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
```
7. 创建启动脚本(run.py)
```python
#!flask/bin/python
from app import app
app.run(debug = True)
```
8. jinjia2模板继承
```
父base.html
{% block body %} {% endblock %}
子xxx.html
{% extends 'base.html'  %}
{% block body %} dosomething {% endblock %}
```

9. 模板中使用url反转
```
{{ url_for('login') }}
```

10. 目录结构，run.py启动脚本，views.py视图函数脚本，utils公共函数脚本，flask虚拟环境文件夹
```bash
├── app
│   ├── db_fun.py
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── static
│   │   └── css
│   │       └── login.css
│   ├── templates
│   │   ├── base.css
│   │   ├── base.html
│   │   ├── dog.jpg
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── regist.html
│   │   └── upd.html
│   ├── util.py
│   ├── util.pyc
│   ├── views.py
│   └── views.pyc
├── config.py
├── day5-执行结果.gif
├── run.py
├── tmp
└── flask 
```

11. 模板
    * index.html首页，显示所有用户信息，带删除和修改功能
    * login.html登录模板
    * regist.html注册模板
    * upd.html修改表单提交模板
