### 需求分析
>   用户权限管理系统

#### 功能模块

##### 首页
> v: index.html
     
     1.reg/login两个导航按钮，连接到登录注册模块
     2.欢迎信息：welcome {{username}}


> c: @app.route('/')
     @app.route('/index/')
     def index():
         username = "wd"
        return render_template("index.html",username=username)

#### 注册页面
v ：reg.html
    <form action=“/reg”,method="post">
      用户名，密码，角色
    </from>
    
c: @app.route('/reg/',method=['GET','POST'])
   def reg():
       if methods为post：
          username = request.form.get('username',"")
          ..............
         if 判断用户是否已经存在
            如果存在则返回错误信息render_template
         else:
            sql
            return rediretc("跳转到登录页面")

         return render_template("reg.html")
m:user
  select * from user where username = username
  insert into user() values()

#### 登录页面
v: login.html
    <form action="login/" ,method="post">
     账号，密码，角色
    </form>
c:@app.route("/login/",methods=['GET','POST'])
def login():
data = { k:v[0] for k,v in dict(request.form).items()}
           result = getone('user',field,data)
if 判断是账号正确
else：执行报错信息

m：登录成功后进入页面 sql = "select * from %s" % table


#### 管理页面/列表
v:userlist.html
   <table>
    用户，密码，角色，操作
    使用jinja2连接 python语句

   <\table>

m：@app.route("/userlist/")
def userlist():


v：sql = "select * from %s" % table

### 更新页面
v：<form>
   输入账号 密码 角色
   点击更新
   <form>

m：@app.route('/update/',methods=['GET','POST'])
def modity():
    得到输入字段 变成字典 条件判断

v：def update(table,field,data):
    condition = ["%s='%s'"%(k,data[k]) for k in data]
    sql = "update %s set %s where id='%s';"%(table,','.join(condition),data['id'])


#### 删除账号
v：userlist.html
   <a href="/del?id={{ user.id }}">删除</a>
m:@app.route('/del/')
def deleteuser():
        uid=request.args.get('id')
        data={'id':uid}
        print data
        result = delete(data)

v:def delete(data):
    sql = "delete from  user  where id='%s';"%(data['id'])
    cur.execute(sql)




