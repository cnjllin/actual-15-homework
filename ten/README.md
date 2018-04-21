    ###  需求分析

>  用户权限管理系统

#### 功能模块

##### 首页/个人信息

V:  index.html
   
    1：reg/login两个导航按钮，连接到登陆注册模块
    2：欢迎信息： welcome  {{username}}

C: @app.route('/')
   @app.route('/index/')
   def index():
      username = "wd"
      return render_template("index.html",username=username)

#### 注册页面

V: reg.html
   <form action=“/reg/”,method="post"> 
    用户名，密码，角色
   </form>

C: @app.route('/reg/',methods=['GET','POST'])
   def reg()
      if methods 为POST:
          username = requset.form.get('username',"")
          ………………
          if 判断用户是否已经存在
             如果存在则返回错误信息render_template("reg.html",error=error)
          else:
             sql 
             return rediret(“跳转到登陆页面”)

      return render_template("reg.html")

M: user
   
   CREATE TABLE `user1` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL UNIQUE,
  `password` varchar(100) NOT NULL,
  `role` int(10) NOT NULL,
  PRIMARY KEY (`id`)
  )  DEFAULT CHARSET=utf8;


   select * from user where username = username
   insert into user () values () 
   


### 登陆页面

V: login.html
   
   <form action="/login/" method="post">
    username  password
   </form>


C: @app.route("/login/",methods=['GET',POST])
   def login():
        if requset.method == "POST":
             user = requset.form 
             res = getone('user',field,user)
             if res['code'] == 0  && res['msg']['password'] = user['password']:
                 ......
             else:
                 .....
        return render_template('login.html')


M: 查某一条数据
   def getone(table,field,data):
      sql = "select * from user where username="wd""

      res = cur.exculte(sql)
      if res :

      eles:
         



### 管理页面/用户列表



### 更新页面




