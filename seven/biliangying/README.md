###  需求分析

>  用户权限管理系统

#### 功能模块

##### 首页

V： index.html
    if not session:
	return redirect('/login/')
    print session
    if session['role']==0:
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
            
                    return redirect('/login/')
          return render_template("reg.html")


M:
    向表内插入用户信息
    def insert(field,data):
        "insert into user (%s) values (%s)" % (','.join(field),','.join(data))

    

##### 登录页面

V:  login.html
    <form action="/login/",method=="post">
    用户名，密码

C:  @app.route('/login/',methods=['GET','POST']
    def register():
        if request.method == 'POST':
            user = {k:v[0] for k,v in dict(request.form).items()}
            res = getone('user1',field,user)
	    if res['code'] == 0:(判断用户是否存在）
		if res['msg']['passwold] == user['password']:（判断密码）
		    session['username'] = user['username']
		    session['role']=result['msg']['role']
		    return redirect('/list/')
		else:
		    返回错误信息密码错误
	    else:
		用户不存在

M: 查某条数据
    def getone(table,field,data)
        sql = "select * from user where username='%s' 
	res=cur.exculte(sql)
        

session:
1、导入session
2、随机数
3、登录成功后创建session








用户名密码是否正确
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

