目录介绍：

app.py  	 	     # 主程序

util.py   		  # 连接数据库，增删改的函数模块

templates         # 放页面的目录

   index.html     # 首页
   
   login.html     # 用户登录页面
   
   register.html  # 注册用户页面
   
   userlist.html  # 展示用户信息页面
   
   update.html    # 更新用户页面


##作业模块拆分：

###注册用户模块：
```
	 1.访问注册url，网站出现注册的页面，提示输入用户名，密码，性别，年龄，手机号，邮件，角色
    2.点击注册的时候，需要做一个判断，如果用户名已经在数据库中，则提示用户已经存在，如果用户不存在    
    数据库中，则执行insert插入操作，然后提示注册成功。（跳转到select查询用户信息的页面，把数据库
    中所有信息展示出来）
```


###登录用户模块：
```
	1.访问登录url,网站出现登录页面，提示输入用户名和密码，需要做一个判断，查询数据库，
	如果用户和密码不正确，则提示用户活着密码不正确，如果用户和密码和数据库中的一致，则提示登录成功，跳转到查询页面。

```

###查询用户模块：
```
	1.访问查询url,网站出现userlist页面，展示数据库中的所有信息。

```

###修改用户模块：
```
	1.访问修改url,网站出现修改的页面，首先需要执行查询操作，然后展示出来所有用户信息，点击修改，
	修改之后，如果用户相同，则提示用户已存在，如果用户名不相同，则修改成功，出现修改信息。
```

###删除用户模块：
```
	1.访问删除url,网站出现删除的页面，点击删除那一个用户信息，用户信息则被删除。
```