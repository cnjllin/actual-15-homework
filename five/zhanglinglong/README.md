
### 作业需求：    

*  用户登录后，通过v端（html）点击查询和删除，有C端（后端脚本），对数据库进行查询与删除

### 思路分析：

* 用户登录成功后，返回用户列表页面
* 通过查找数据库，返回用户列表信息,并且后面附带删除与更新密码
* 定义更新的页面，通过更新，对数据库进行操作


### 作业说明：

├── liucheng.png        流程示意图
├── login_register.py   作业脚本
├── README.md           文件目录说明
├── templates           存放html文件
│   ├── login.html      登录页面
│   ├── register.html   注册页面
│   ├── update.html     更新页面
│   ├── userlist.html   用户列表（数据库中查询）
│   └── welcome.html    欢迎页面
└── user.txt            用户登录列表