## 项目需求

* 实现用户HTML注册登录写入数据库
* HTML对用户管理（增删改查）

## 项目分析
* 一共4个主页面+3个返回信息页面
* 首页--提交登录/注册
* 注册--提交用户注册信息（用户名，密码，手机号，email,role）
* 登录--提交用户、密码
* 管理--（admin管理用户）
    * 查询用户信息
    * 查询个人信息（修改密码）
* 普通用户--（普通user）
    * 个人信息查询

## 项目实现
* 首页
    * @app('/')
    * @app('/index')        
        * 返回注册/登录页面,并返回registor/login HTML页面
* 注册
    * registor.html表单提交（post）数据
    * @app.route('/registor' methods=['GET','POST'])，判断表单请求
        * POST,获取用户名/密码传入功能函数 utl.py判断用户是否存在，并返回判断。若用户不存在，return到登录页面；否则，返回错误信息给前端registor.html
        * GET，返回registor.html
* 登录
    * 前端login.html提交用户名密码
    * @app.route('/login',methods=['GET','POST'])
        * POST:获取用户名/密码传入功能函数，util.py判断用户密码是否正确，正确返回res={'code':0}；Python再判断用户是否为管理员，若role=0,返回管理员权限页面manager.html；role=1，返回普通用户权限页面userinfo.html
        * GET:返回login.html
* admin用户管理
    * @app.route('/selectusers'):查询数据库user表中所有用户信息并返回给userlist.html页面显示
        * 用户删除： @app.route('/delete')：delete.html表单get方式提交id给后端，根据ID操作数据库删除用户
        * 更改用户密码： @app.route('/update')：GET方式传入ID 
            * 表单提交方式为GET，返回update.html，两次输入密码确认post提交
            * 表单提交方式为POST,再判断两次密码是否相同，返回判断信息给update.html
    * @app.route('/oneuser'):返回用户个人信息给oneuser.html
* 普通用户
    * 查询个人信息：@app.route('/oneuser')返回用户个人信息给oneuser.html

        
## 目录结构
```
├── homework5v1.py
├── templates
│   ├── index.html
│   ├── login.html
│   ├── manager.html
│   ├── oneuser.html
│   ├── registor.html
│   ├── update.html
│   ├── userinfo.html
│   └── userlist.html
├── util.py
└── util.pyc
```
