### 需求分析

>  用户权限关系系统

### 功能模块

#### 首页
```
V: index.html
   1: reg/login 两个导航按钮,链接到登录注册模块
   2: 欢迎信息：welcom {{ username}}
C: @app.route('/')
   @app.route('/index/')
   def index():
       username = 'wd'
       return render_template("index.html",username=username)
```
#### 注册页面
```
V: reg.html
   <form action="/reg/", method="post">
   用户名,密码,角色
   </form>
C: @app.route('/reg/',methods=['GET','POST'])
   def reg():
       if methond == post:
            username = request.form.get('username',"")
            …………
           if 判断用户是否存在
              如果存在则返回错误信息，render_template('reg.html',err=err)
            else:
               sql
                return rediret('跳转到登录页面')
             return render_template('reg.html')
M: user
   
   select * form user
   insert into user () values ()
```
#### 登录页面
```
V: login.html
    <form action ='/login/',method='post'>
     username  passwd
     </form>

C: @app.route("/login/",methods=['GET','POST'])
   def login():
        if resust.method == 'POST':
           user = requset.form
           res  = getone('user',filed,user)
           if res['code'] == 0 && res['msg']['password'] = user['password']:
                ...
            else:
                ...
          return render_template('login.html')
M: 查某一条数据
   def getone(table,filed,data):
       sql = "select * from user where username='wd'"
       res = cur.exculte(sql)
       if res:
              ...
        else:
             ...
```
#### 管理页面/用户列表
    

#### 更新页面


