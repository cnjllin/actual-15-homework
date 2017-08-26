#!/usr/bin/env python
#coding:utf-8
'''
作业需求：
基于mysql数据库实现用户登录模块，并实现针对于用户信息的增删改查
'''


from flask import Flask,render_template,request,redirect
import MySQLdb as mysql

app = Flask(__name__)

# 连接数据库的固定用语
conn = mysql.connect(host='127.0.0.1',user='root',passwd='123456',db='reboot15',port=3306)
conn.autocommit(True)
cursor = conn.cursor()

# 主页并显示当前用户所有的信息
@app.route('/')
@app.route('/index/')
def index():
	welcome = "Welcome to the page!"
	sql = "select * from  user"
	cursor.execute(sql)
	res = cursor.fetchall()
	return render_template("index.html",welcome=welcome,res=res)

# 用户登录认证页面
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('yourname','None')
		password = request.form.get('yourpasswd','None')
		sql = 'select * from user where username=%s and password=%s'
		if cursor.execute(sql,(username,password)):
			res = "Welcome to login."
			return render_template("success.html",res=res)
		else:	
			res = 'Your username and password is wrong.'
			return render_template("success.html",res=res)
	else:
		return render_template("login.html")

# 用户注册插入数据页面
@app.route('/register/', methods=["GET","POST"])
def register():
	if request.method == 'POST':
		username = request.form.get('yourname')
		password = request.form.get('yourpasswd')
		repassword = request.form.get('reyourpasswd')
		sex = request.form.get('sex')
		age = request.form.get('age')
		phone = request.form.get('phone')
		email = request.form.get('email')
		role = request.form.get('role')
		if password == repassword:
			sql = 'insert into user (username,password,sex,age,phone,email,role) values ("%s","%s","%s","%s","%s","%s","%s")' % (username, password,sex,age,phone,email,role)
			cursor.execute(sql)
			res = "Congratulations on your registration is success. %s"  % username
			return render_template("success.html",res=res)
		else:
			res = "Your username or password is worong."
			return render_template("success.html",res=res)
	return render_template("register.html")

# 用户删除信息页面
@app.route('/del/',methods=['GET','POST'])
def del_user():
	if request.method == 'GET':
		user_id = int(request.args.get('id'))
		sql = 'delete from user where id =%d' % user_id
		cursor.execute(sql)
	return redirect('/index/')


# 用户更新信息页面
@app.route('/update/',methods=['GET','POST'])
def update_user():
	if request.method == 'GET':
		user_id = int(request.args.get('id'))
		return render_template('update.html',user_id=user_id)
	if request.method == 'POST':
		username = request.form.get('yourname')
		password = request.form.get('yourpasswd')
		repassword = request.form.get('reyourpasswd')
		user_id = request.form.get('id')
		if password == repassword:
			sql = 'update user set password=%s where id =%s' %(password,user_id)
			cursor.execute(sql)
			return redirect('/index/')
		else:
			return render_template('success.html',res='Your update is failed')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=1234,debug=True)
