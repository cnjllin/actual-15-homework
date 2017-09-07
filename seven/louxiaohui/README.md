### 需求分析

> 用户权限管理系统

### 功能模块


#### 首页

view: index.html

      1：reg,login两个导航按钮,链接到登陆注册模块
      2：欢迎信息: welcome {{ username }}

control: @app.route('/')
         @app.route('/index/')
         def index():
             username = "wd"
             return render_template("index.html",username=username)

#### 注册页面
view: reg.html
      <form action="reg",method="post">
      用户名，密码，角色
      </form>
control: @aap.route('/reg/',methods=['GET','POST'])
         def reg():
             if method="post":
                 username = request.form.get('username',"")
                 if 判断用户是否已经存在:
                     如果存在则返回错误信息render_template("reg.html",error)
                 else:
                     sql
                     return redirec("跳转到登陆界面")
            return render_template("reg.html")

model: user
       select * from user where username = username
       insert into user () values ()

#### 登陆页面

V: login.html
   <form action="/login/" method="psot">
   username password
   </form>

C: @app.route("/login/",method=['GET','POST')
   def login():
       if request.method == "POST"
           user = request.form
           res = = getone('user',field,user)
           if res['code'] == 0 && res ['meg']['password'] == user['password']
               ....
           else:
               ....
       return render_template('login.html')
          
M:查某一条数据
    def getone(table,field,data):
        sql = "select * form user where username='wd'"
        cur.execute(sql)
        res = cur.execute(sql)
        if res:
            ....
        else:
            
        

#### 管理页面/用户列表

#### 更新页面


