###  需求分析

>  用户权限管理系统

#### 功能模块

##### 首页

V： index.html
    
    1、登录/注册两个导航按钮，连接到登录注册模块
    2、欢迎信息：welcome  {{username}}

C:  @app.route('/')
    @app.route('/index/')
    def index():
        username = 'wd'
        return render_template("index.html",username=username)

##### 注册页面

V： register.html
    <form action="/reg/",method=="post">
    用户名，密码，手机号，邮箱，角色
    </form>
    

C:  @app.route('/reg/',methods=['GET','POST']
    def register():
        if method = POST:
            user = {k:v[0] for k,v in dict(request.form).items()}
            判断用户名是否为空
                为空返回错误信息
            判断用户名是否存在
                存在返回错误信息
            else:
                判断密码是否小于6位
                    存在返回错误信息
                判断密码是否正确
                    错误返回错误信息
		else:
		    删除user中的键repassword
		    写入到数据库中
                    return redirect('/login/')
          return render_template("reg.html")


M:  判断用户是否存在
    def judgeuser(user):
        "select * from user where username='%s'" % user["username"]
    向表内插入用户信息
    def insert(field,data):
        "insert into user (%s) values (%s)" % (','.join(field),','.join(data))

    

##### 登录页面

V:  login.html
    <form action="/login/",method=="post">
    用户名，密码

C:  @app.route('/login/',methods=['GET','POST']
    def register():
        if method = POST:
            user = {k:v[0] for k,v in dict(request.form).items()}
            判断用户是否存在:
		存在判断密码角色：
			密码正确角色为管理员，return redirect('/list/')
			密码正确角色为普通用户，return redirect('/getone/')
	         else:
			密码错误返回错误信息
	    else:
	        用户不存在返回错误信息

M:  用户名密码是否正确
    def login(user):
	 sql = "select * from user where username='%s' and password='%s'" % (user["username"],user["password"])
    判断角色
    def role(user):
	sql = "select * from user where username='%s'" % user["username"]
		        
##### 管理页面/用户列表
V:  list.html
    <form action="/login/",method=="post">
    ID,用户名，密码,邮箱，手机号，角色
    {% for i in user %} {{user.id}}{{user.username}}.....{% endfor %}
    <a href="/update/?id={{ i.id }}">更新</a> 
    <a href="/delete/?id={{ i.id }}">删除</a> 
   
    
C:  @app.route('/list/')
    def list():
        查询用户信息
        return render_template('list.html',user=user)

M:  用户信息
    def userlist():
        field = ['id','username','password','tel','email','role']
        sql = "select * from user"
        user = [{k:row[i] for i,k in enumerate(field)}for row in res]


##### 更新页面
V:  update.html
    <form action="/update/" method="POST">
    id(hidden)用户名，密码，邮箱，手机号
     value='{{user.id}}'


C:  @app.route('/update/',methods=['GET','POST'])
    def update()
        获取用户id
        if request.method=="GET":
                uid = request.args.get('id','')
		查询用户信息
                return render_template('update.html',user=user)
	修改用户信息
        if request.method=="POST":
                user = {k:v[0] for k,v in dict(request.form).items()}
		用户信息更新到数据库
                return redirect('/list/')

M:  通过id查询用户信息
    def inquire(uid):
        sql = "select * from user where id=%s" % uid
    修改用户信息
    def update(user):
        conditions = ["%s='%s'" % (k,user[k]) for k in user]
        sql = "update user set %s where id = %s" % (','.join(conditions),user['id'])


##### 删除用户信息

C:  @app.route('/delete/',methods=['GET','POST'])
def delete():
        if request.method=="GET":
                uid = request.args.get('id','')
		return redirect('/list/')
        return render_template('list.html')

M:  def delete(uid):
        sql = "delete from user where id=%s" % int(uid)
