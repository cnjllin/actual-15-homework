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
  

2. 资产模块(cmdb)
  * 机房模块
    * 显示机房信息，添加、更新、删除机房信息
  * 机柜模块
    * 显示机柜信息、添加、更新、删除机柜信息
  * 服务器模块
	* 显示服务器信息、添加、更新、删除服务器信息

3.  工单模块
  * 工单列表
  * 添加工单、
  * 更改工单状态


### 项目结构
```
.
├── app
│   ├── cabinet.py
│   ├── idc.py
│   ├── __init__.py
│   ├── job.py
│   ├── __pycache__
│   ├── server.py
│   ├── static
│   ├── templates
│   └── user.py
├── config.py
├── db.py
├── images
│   ├── cabinetadd.PNG
│   ├── cabinet_del.PNG
│   ├── idc_add.PNG
│   ├── idc_update.PNG
│   ├── server_update.PNG
│   ├── updateuser.PNG
│   └── userlist.PNG
├── __pycache__
│   ├── config.cpython-35.pyc
│   ├── db.cpython-35.pyc
│   └── utils.cpython-35.pyc
├── README.md
├── run.py
├── tmp
│   └── test.log
└── utils.py

```

### 用户列表页
![](https://github.com/51reboot/actual-15-homework/raw/master/nine/yangyi/images/userlist.PNG)

### 用户更新页
![](https://github.com/51reboot/actual-15-homework/raw/master/nine/yangyi/images/updateuser.PNG)

### 机房添加页
![](https://github.com/51reboot/actual-15-homework/raw/master/nine/yangyi/images/idc_add.PNG)

### 机房更新页
![](https://github.com/51reboot/actual-15-homework/raw/master/nine/yangyi/images/idc_update.PNG)

### 机柜添加页
![](https://github.com/51reboot/actual-15-homework/raw/master/nine/yangyi/images/cabinetadd.PNG)

### 机柜删除页
![](https://github.com/51reboot/actual-15-homework/raw/master/nine/yangyi/images/cabinet_del.PNG)

### 服务器更新页
![](https://github.com/51reboot/actual-15-homework/raw/master/nine/yangyi/images/server_update.PNG)