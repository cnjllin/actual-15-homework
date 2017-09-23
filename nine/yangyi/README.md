## 作业
```
CMDB  增加对用户访问和数据操作异常的记录
```

### 项目分析

1. 用户模块
  * 个人中心
    * 显示个人信息 修改个人信息
  * 用户列表
    * 管理员查看所有用户信息，修改用户信息，删除用户
  

2. 资产模块
  * 机房模块
    * 显示机房信息，添加、更新、删除机房信息
  * 机柜模块
    * 显示机柜信息、添加、更新、删除机柜信息


### 项目结构
```
.
├── app
│   ├── cabinet.py    # 机柜模块
│   ├── idc.py    # 机房模块
│   ├── __init__.py  # 入口函数
│   ├── __pycache__
│   │   ├── cabinet.cpython-35.pyc
│   │   ├── idc.cpython-35.pyc
│   │   ├── __init__.cpython-35.pyc
│   │   └── user.cpython-35.pyc
│   ├── static    # 静态文件目录
│   │   ├── css
│   │   ├── img
│   │   ├── js
│   │   └── plugin
│   ├── templates    # 模板文件目录
│   │   ├── cabinet    # 机柜模块 HTML 目录
│   │   ├── common    # 公共模块 HTML 目录
│   │   ├── idc    #  机房模块 HTML 目录
│   │   └── user    # 用户模块 HTML 目录
│   └── user.py    # 用户模块
├── config.py      # 配置文件
├── db.py    # 数据库模块
├── __pycache__
│   ├── config.cpython-35.pyc
│   ├── db.cpython-35.pyc
│   └── utils.cpython-35.pyc
├── run.py    # 运行
├── tmp    # 日志存放目录
│   └── test.log    # 日志
└── utils.py    

```