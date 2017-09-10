### 项目结构：  
    [root@Python01 gaofan]# tree
    .
    ├── app.py                  #主程序文件
    ├── config.py               #配置文件
    ├── exts.py                 #扩展文件，存放数据库和app等对象
    ├── models.py               #数据库模型
    ├── static                  #静态文件目录
    │   ├── bootstrap.css       #css库文件
    │   ├── images              #图片
    │   │   ├── loginBac.jpg
    │   │   └── login.jpg
    │   ├── login.css           #登录界面css
    │   └── login.js            #登录界面js
    ├── templates               #html模板文件
    │   ├── admin.html          #管理员登陆后界面
    │   ├── login.html          #登录界面
    │   ├── member.html         #普通用户登录界面
    │   ├── reg.html            #注册界面
    │   └── update.html         #更新界面
    └── utils.py                #功能模块函数

## 项目分析：
* 采用flask_sqlalchemy来连接数据库；
* 注册页面  
    * 关键点：   
    V端：POST请求，form表单  
    C端：获取form参数，拼接成字典形式
    M端:调用功能模块函数user_add()入库
    注意的地方：用户名检查机制user_check(不能重复)和密码检查机制passwd_check（保持一致）
    相关错误信息会在界面显示
* 登录页面
    * 关键点：  
    V端：POST请求，form表单  
    C端：获取form参数，拼接成字典形式  
    M端：数据库中user_get()比较当前的输入用户名和密码  
    相关错误信息会在界面显示  
    登录成功：  
    1，普通用户只能看见自己信息  
    2，管理员可以看到所有用户信息，并且可以更改
* 更改页面  
    * 关键点：  
    V端：POST请求，form表单  
    C端：获取form参数，拼接成字典形式   
    M端：调用功能模块函数user_update()入库  
     注意的地方：用户名检查机制user_check(不能重复)和密码检查机制passwd_check（保持一致）  
    相关错误信息会在界面显示
* 删除页面  
    * 融合在更改页面，只有管理员有权限删除，根据user_delete删除；
* session机制
    * 若session过期或者不存在，必须先登录  
* 操作演示：  
![](ttps://github.com/51reboot/actual-15-homework/blob/master/seven/gaofan/result3.gif)