## 目录结构
```
├── app
│   ├── 123.sql
│   ├── code.py  验证码生成
│   ├── code.pyc
│   ├── db_fun.py
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── passwd_hash.py
│   ├── passwd_hash.pyc
│   ├── static
│   │   ├── css
│   │   │   ├── index.css 首页样式
│   │   │   └── login.css 
│   │   └── image
│   │       └── idencode.png  验证码图片
│   ├── templates 模板文件
│   │   ├── base.css
│   │   ├── base.html 基础模板
│   │   ├── dog.jpg
│   │   ├── idencode.png
│   │   ├── index.html
│   │   ├── index.html.bak
│   │   ├── login.html
│   │   ├── quest.html
│   │   ├── regist.html
│   │   ├── upd.html
│   │   └── userlist.html
│   ├── util.py  数据库操作
│   ├── util.py.bak
│   ├── util.py_bak20170831
│   ├── util.pyc
│   ├── views.py  视图函数
│   ├── views.py~
│   ├── views.py_0830
│   └── views.pyc
├── config.py
├── day6-0831.gif
├── idencode.png
├── README.md
├── run.py  运行程序
└── flask 虚拟环境
```
***

## 模块说明
* **基础模板** `base.html`，其他模板继承导航航条，title后缀，bootstrap样式
> 导航栏:首页  发表文章  文章查找  登录/用户信息  注册/注销  

* **首页** 
    - 功能：显示文章、查找文章，路由：`'/'`、`'/index/'`,模板文件：`index.html`
> 模板继承显示导航栏，`get`请求返回所有文章列表  
`post`请求根据关键字查找文件

* **注册**  
  - 功能：注册用户，加密密码，数据库保存用户信息，路由：`'/regist/'`,模板文件：`regist.html`
> 模板继承显示导航栏，`get`请求返回当前页面  
`post`请求提交表单，验证用户名是否存在，两次密码是否一致，验证码是否正确，然后加密密码保存数据库,注册成功跳转到登录页面

* **登录**  
  - 功能：登录用户，保存session31天，路由：`'/login/'`,模板文件：`login.html`
> 模板继承显示导航栏，`get`请求返回当前页面  
`post`请求提交表单，验证用户名是否存在，密码是匹配，验证码是否正确，登录成功跳转到首页

* **用户列表**
  - 功能：显示用户列表，提供删除修改用户链接，路由：`''/userlist/''`,模板文件：`userlist.html`
> 模板继承显示导航栏，`get`请求当前用户管理员，返回所有用户列表，普通用户返回该用户信息返，
>> 带有删除超链接，通过get请求`'/dele/'`删除用户  
通过提交表单到`'/upd/'`修改用户信息

* **删除用户** 
  - 功能：删除用户，路由：`'/dele/'`,模板文件：`无`，首页超链接？id=xx传uid
> 模板继承显示导航栏，`get`请求/dele/?id=xx传输用户id号删除用户，需要登录


* **修改用户** 
  - 功能：修改用户，路由：`'/upd/'`,模板文件：`upd.html`
> 模板继承显示导航栏，`get`请求返回当前页面  
接收用户列表页面`post`请求表单，修改用户信息

* **发表文章**
  - 发表文章，保存articles表，路由：`'/article/'`,模板文件：`quest.html`
> 模板继承显示导航栏，`get`请求返回当前页面  
`post`请求提交表单，保存用户发表文章


* **退出登录**
  - 功能：退出登录，路由：`'/logout/'`,模板文件：`无`，接收base.html请求
> 显示在导航栏，`get`请求清除session退出登录跳转到首页

***