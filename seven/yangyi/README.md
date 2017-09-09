# 第七天作业

作业：
    对第六天实现的功能进行页面展示的优化

## 项目模块分析

 1.登录

 2. 退出

 3. 用户管理
   - 普通用户
    * 个人中心
       查看个人信息、更改个人信息
   - 管理员
     * 个人中心
        查看个人信息、更改个人信息
     * 用户列表
       查看用户信息、删除用户、更改用户信息、添加用户

## 项目功能分析
1. login()
   * 请求方式是否为 POST
   * 获取用户输入
   * 判断用户信息是否正确
   * 将用户信息存入 session 返回信息

 2. adduser()
       * 请求方式是否为 POST
       * 将新增用户信息转为字典形式
       * 判断新增用户是否符合要求
       * 将符合要求的用户信息存入数据库并返回成功信息

 3. userlist()
       * 从session中获取role
       * 根据role 取值不同从数据库中获取不同的 user 并返回不同的页面

  4. userself()
        * 从session中获取 role id
        * 获取用户信息并传至 userself.html
        * 根据role 的不同 修改密码时的规则不同 普通用户需要确认原始密码

   5. update_msg()
        * 获取前端传的 id 根据 id 查询更新用户信息
        * 将从数据库中获取的数据传入弹窗

   6. update()
        * 获取用户输入
        * 将更新信息写入数据库
        * 返回写入结果

    7. modpwd()
        * 获取用户输入
        * 判断用户输入格式
        * 格式正确更新数据库返回更新信息

##项目结构
```
.
├── app.py
├── __pycache__
│   └── utils.cpython-35.pyc
├── README.md
├── static
│   ├── css
│   ├── img
│   ├── js
│   └── pulgin
├── templates
│   ├── add.html
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── userlist.html
│   └── userself.html
└── utils.py
```
