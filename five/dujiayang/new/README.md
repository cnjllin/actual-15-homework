## 需求分析

> 用户权限管理系统

#### 功能模块

##### 首页

V: index.html
	1:reg and login 2个导航button，链接到登录注册模块
   	2:欢迎信息：welcome {{username}}

C: 	@app.route('/')
	@app.route('/index/')	
	def index():
		username = "wd"
		return render_template("index.html",username=username)
	
	
##### 注册页
V: reg.html
	<form action="/reg/" method="post">用户名，密码,角色</form>

C:@app.route('/reg/',methods=['GET','POST'])
  def reg():
	if method == 'POST':
		username = request.form.get('username',"")
		....
		if判断用户是否存在
			error = ""
			存在，返回错误信息render_template("reg.html",error=error)
		else:
			sql
			return render_template("跳转到登录页面")

M:user
	select * from user where username = username
	insert into user() values()
	
	
##### 登录页
##### 管理页
