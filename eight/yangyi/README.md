# 第八天作业

作业：

通过对网络上的页面进行复制以及使用js美化个人作业

## 项目分析

1. 用户管理
    * 个人中心
        * 显示个人信息,同时可以修改个人中心
    * 用户列表
        * 显示所有用户信息同时可以添加和修改用户信息


2. 资产管理
    * 机房管理
        * 显示已有机房信息，同时可以添加机房(其他模块未作)


## 项目功能分析

### 公共模块
1. 登录/退出
    *  login()
    *  logout()
2. 用户模块
    * 个人信息 ： userinfo()
    * 用户列表 ： userlist()
    * 添加用户 ： useradd()
    * 更新和删除 ： update() 、delete()

3. 资产模块
    * 机房列表： idc()
    * 添加机房： idcadd()

### 目录结构
```
.
├── app.py
├── config.py
├── __pycache__
│   ├── config.cpython-35.pyc
│   └── utils.cpython-35.pyc
├── README.md
├── static
│   ├── css
│   ├── img
│   ├── js
│   └── plugin
├── templates
│   ├── add.html
│   ├── base.html
│   ├── idcadd.html
│   ├── idclist.html
│   ├── index.html
│   ├── login.html
│   ├── userinfo.html
│   └── userlist.html
└── utils.py

```
