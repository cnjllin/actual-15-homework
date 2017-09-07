# 51reboot 登陆注册项目文档
## 一、项目概述
- 首页是一个index.html ，判断新用户或者老用户
- 新用户跳转到reg.html ,进行注册模块操作，注册模块分为：
  - 注册页面
  - 注册函数
- 老用户跳转到login.html,进行登陆模块操作，登陆模块分为：
  - 登陆页面
  - 登陆函数
- 登陆成功跳转到会员中心模块userlist.html.
  - 会员中心页面
  - 会员中心函数
  - 会员中心-更新页面
  - 会员中心更新函数
  - 会员中心-删除函数
## 二、需求分析
- 访问首页时身份判断，根据访问者身份做页面跳转
- 访问注册页面出现三个输入框：用户名，密码，密码确认 。判断如果用户不存在，两次输入的密码相同注册成功，否则失败并给出提示。
- 访问登陆页面出现两个输入框：用户名，密码 。登陆成功跳转到会员中心页面；登陆失败给出提示
- 会员中心页面是更新后的库文件以表格页面形式展示
- 对会员中心页面进行提交表单增加删除和更新操作
## 三、模块拆分
- 注册模块
    - 注册页面 只做渲染reg.html处理，reg.html的form action部分匹配注册表单部分
    - 注册表单 flask框架中对页面提交的信息进行操作和结果判断，如果成功：f.write("%s:%s \n" % (username,user_pass1)) 并且 将结果渲染给reg.html render_template('reg.html',ok='Congratulations on your successful registration') 。失败：只需将结果渲染给reg.html render_template('reg.html',ok='regist failed,agine')
- 登陆模块
    - 登陆页面 只做渲染login.html处理，login.html的form action部分匹配登陆表单
    - 登陆表单 flask框架中对页面提交的信息进行操作和结果判断，如果成功： redirect('/userlist/') ，失败则把错误信息渲染给登陆页面render_template('login.html',error='username or password is error')
- 会员中心首页模块
    - 以注册模块生成的user_message.db为数据基础，在flask框架中以[h1[0]:h1[1],h2[0]:h2[1],...]的形式渲染给userlist.html,在html中通过{% for循环 %}，<table> 将结果以表格的形式展示出来
- 会员中心-更新模块
        - 根据提交的信息验证用户名密码是否可以锁定一个对象。是则update 数据库。否则返回报错信息
- 会员中心-删除模块
        因是get方式传参，可以在html中设置href 跳转到框架中的应用。进而更新到后端库文件。
- 用户校验模块  嵌入到注册和登陆模块中。
    - 用户名和密码校验函数
    - 用户是否存在函数
## 四、项目代码规范：
 ```   .
home_task/
├── 51reboot 登陆注册项目文档.md
├── flask2login.zuoye.20180825.py
├── my_mysql.py
├── templates
│   ├── index.html  
│   ├── login.html
│   ├── reg.html
│   ├── update.html
│   ├── userlist.html
│   └── userlist.html.1
├── userconf.py
├── userconf.pyc
├── userinfo.py
├── userinfo.pyc
└── user_message.db
```