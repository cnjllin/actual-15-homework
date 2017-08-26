#!/usr/bin/python
#coding:utf-8
from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
db=mysql.connect(host="127.0.0.1 ",user="root",passwd="123",db="reboot15",port=3306,charset='utf8')
db.autocommit(True)
cur = db.cursor()
app = Flask(__name__)
# 首页
@app.route('/')
def welcome():
        return render_template('welcome.html')
# 注册
@app.route('/reg/',methods=['GET','POST'])
def register():
	errmsg1 = u"用户名存在"
	errmsg2 = u"密码不一致 "
	sql = "select * from user"
	cur.execute(sql)
	a = []
	for i in cur.fetchall():
		a.append(i[1])
	if request.method=="POST":
		username = request.form.get('username')
		age = request.form.get('age')
		phone = request.form.get('phone')
		email = request.form.get('email')
		passwd1 = request.form.get('passwd1')
		passwd2 = request.form.get('passwd2')
		if username not in a:
			if passwd1 == passwd2:
				cur.execute("insert into user values (' ',%s,%s,%s,%s,%s)", [username,passwd1,age,phone,email])
				return redirect('/login/')
			else:
				return render_template('register.html',errmsg2=errmsg2)
		else:
			return render_template('register.html',errmsg1=errmsg1)
	return render_template('register.html')
# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
	errmsg1 = u"密码错误"
	errmsg2 = u"用户不存在"
	sql = "select * from user"
	cur.execute(sql)
        a=[]
        b={}
        for i in cur.fetchall():
		a.append(i)
        for j in a:
                b[j[1]]=j[2]
	if request.method=="POST":
        	username = request.form.get('username')
		passwd = request.form.get('passwd')
		if username in b.keys():
			if passwd == b[username]:
				return redirect('/hehe/')
			else:
				return render_template('login.html',errmsg1=errmsg1)	
		else:
			return render_template('login.html',errmsg2=errmsg2)
	return render_template('login.html')
# 用户列表
@app.route('/hehe/')
def ip():
	sql = "select * from user"
	cur.execute(sql)
	res = cur.fetchall()
        return render_template('index.html',res=res)
# 删除信息
@app.route('/delete/',methods=['GET','POST'])
def delete():
	if request.method=='GET':
		userid = request.args.get('id','')
		print userid
		sql = "delete from user where id=%s" % int(userid)
		print sql
		cur.execute(sql)
		return redirect('/hehe/')
	return render_template('index.html')
# 修改密码
@app.route('/update/',methods=['GET','POST'])
def update():
	if request.method=='GET':
		userid = request.args.get('id','')
		print userid
		return render_template('update.html')
	global userid
	if request.method=='POST':
              	passwd1 = request.form.get('passwd1')
              	passwd2 = request.form.get('passwd2')
		if passwd1 == passwd2:
			sql = "update user set password=%s where id=%s" % (passwd1,userid)
			cur.execute(sql)
			return redirect('/hehe/')
		else:
			errmsg = u"密码不一致，请重新输"
			return render_template('update.html',errmsg=errmsg)
	 	return render_template('update.html')
if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5550,debug=True)
