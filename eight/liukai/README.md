#  作业
###  扒页面

# 目录结构

<pre>

├── README.md              # 测试文档及项目文档
├── test                   # 测试结构图片
├── show_create_table.md   # 表结构
├── static                 # 静态文件
│   ├── css
│   ├── img
│   ├── js
│   └── pulgin
├── templates             # html
│   ├── add.html          # 添加用户界面
│   ├── index.html        # 首页
│   ├── list.html         # 用户界面
│   ├── login.html        # 登录界面
│   ├── reg.html          # 注册界面
│   └── userlist.html     # 用户列表
├── utils.py              # 功能函数

</pre>


# 测试结果

#### 主界面

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/index.png)

#### 注册界面 

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/reg.png)

#### 注册失败

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/reg_error.png)

#### 注册成功

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/reg_ok.png)

#### 登录界面

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/login.png)

#### 登录失败

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/login_error.png)

#### 登录成功

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/login_ok.png)

#### 管理员界面

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/admin.png)


#### 修改个人资料

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/修改个人资料.png)

#### 用户列表

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/userlist.png)

#### 编辑用户信息

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/编辑用户信息.png)

## 删除用户

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/删除用户.png)

## 添加用户

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/添加用户.png)

## 普通用户界面

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/普通用户.png)



# 项目文档

## 需求分析

> 用户权限管理系统

## 功能模块

### 首页

V: index.html

	1. reg/login两个导航按钮，会连接到登录注册模块
	2. 欢迎信息：wlcome {{username }}
C端
<pre>
@app.route('/') 
@app.route('/index/')
def index():
    username="wd"
    return render_template("index.html",username=username)
</pre>

### 注册页面
V端：reg.html
<pre>
  <\form atction"/reg/",method="POST">
    用户名，密码，角色
  <\/form>
</pre>   
 
C端：
<pre>
@app.route("/reg/",methods=['GET','POST'])
def reg():
    if  method为POST：
        username=request.form.get('username','')
		.........
        if  判断用户是否存在
            如果存在则返回错误信息render_template("reg.html",error=error)
        else:
            sql
            return rediret("跳转到登录页面")
    return render_tempalte("reg.html")
</pre>  

M端:user
<pre>
 mysql> CREATE TABLE `user` (
 ->   `id` int(100) NOT NULL AUTO_INCREMENT,
 ->   `username` varchar(100) NOT NULL,
 ->   `password` varchar(100) NOT NULL,
 ->   `role` int(10) NOT NULL,
 ->   PRIMARY KEY (`id`)
 -> )  DEFAULT CHARSET=utf8;

select * from user where username=username
insert into user () values()
</pre>

#### 登录页面
V端: login.html
<pre>
    <\form atction '/login/',method="POST">
        用户名，密码
    <\/form>
</pre>

C端:
<pre>
@app.route("/login/",methods=["GET","POST"]
def login():
    if method为post：
       username=request.form.get("username"," ")
       password=request.form.get("password"," ")
       if 判断用户是存在并且密码正确：
             if role==1:
                user_dict=查询所有用户信息,并转换为字典
                return render_template("user_list.html",user_dict=user_idct,usaername=username,role=role)
             else:
                user=按用户名查询单用户信息
                return render_template("user.html",user=user)
       
       else：
           msg=用户或密码错误
           return redicet("/login/?msg='用户名或密码错误'")
    return render_tempalte("login.html")
</pre> 

M端:  
<pre>
查所用户信息 sql=" select * from user"
按username 查单用户信息 sql= "select * from user where username=%s"%username
</pre>

## 管理页面/用户列表
    
### 管理员界面    
V端: 
<pre>
1. 左部分 ----><font color=red>显示管理员功能/普通用户更能</font>

2. 右部分 
list.html （右边一个表格显示所有用户信息） 
id ，用户名 ，密码， 权限 ，操作（删除，修改） 
{% for i in user_dict %}                                
  {{ user_dict.id}} ,{{user_dict.username}},{{user_idct.password}},{{user_dict.role}}<\a href="/delete/?id={{user_dict.id }}">删除</a><\a href="/update/?id={{}user_dict.id}">修改</id>
{% endfor %}
</pre>        
     
C端：
<pre>
@app.route("/delete/")
def delete():
    id=request.args.get("id"," ")
        执行删除函数
    return render_tempalte("user_list.html")
</pre>

M端: 
<pre>
sql="delete from user where id=%s"%id
</pre>

### 删除界面
V端： 在list.html上有个按钮，删除后直接跳到登录界面

C端： 获取前端id，根据执行删除sql，然后跳转到login.html

M端： sql="delete from %s where id =%s"%(table,uid)

### 更新页面
V端: update.html

   显示一个表格(名称 ，信息) ,信息内容可改，最下方有个提交按钮（跳转到管理员页面）
                                            
C端:
<pre>
@app.route("/update/")
def update():
    user=执行查询单用户sql，
        return  render_tempalte('update.html'user=user)

@app.route("/update/")
    获取修改的数据
    执行update sql 更改数据库
            
    return render_template("跳转登录界面")
       
  普通用户同上 
</pre>  

M端：
<pre>
  sql="select * from user where id=%s"%id
  
  sql="update user set password='%s',sex=%d,age=%d,phone=%d,email='%s',role=%d where id=%d"%(my_tup[0],my_tup[1],my_tup    
</pre>       


