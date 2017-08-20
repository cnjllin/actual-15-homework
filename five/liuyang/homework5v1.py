#/bin/env python
#coding=utf-8

from flask import Flask,request,render_template,redirect
import util
import MySQLdb as mysql
conn=mysql.connect(host='127.0.0.1',user='root',passwd='piptest',db='liuyang',port=6666,charset='utf8')
conn.autocommit(True)
cur=conn.cursor()

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	hello = 'Welcome !'
	return render_template('index.html',hello=hello)

@app.route('/registor',methods=['POST','GET'])
def registor():
	if request.method == 'POST':
		user_dict = {}
		table_list=['username','password','age','phone','email','role']
		for i in table_list:
			user_dict[i] = request.form.get(i)
		res = util.registorcheck(**user_dict)
		print user_dict
		print res
		if res['code'] == 0:
			value = ','.join(map(lambda x: '\'' + x + '\'', user_dict.values()))
			print '-'*10+ value
			insert_sql = 'insert into user(%s) values (%s);'%(','.join(user_dict.keys()),value)
			print '-'*10+insert_sql
			cur.execute(insert_sql)
			return redirect('/login')
		elif res['code'] ==1 :
			print res['msg']
			return render_template('registor.html',res=res)
	else:
		res={'msg':''}
		return render_template('registor.html',res=res)

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		res = util.logincheck(username,password)
		print res
		if res['code'] == 0:
			sql='select role from user where username="'"%s"'";'%(username)
			cur.execute(sql)
			role = cur.fetchone()
			print role[0]
			if role[0] == 0:
				return redirect('/manager')
			else:
				print username
				return render_template('userinfo.html',username=username)
		else:
			return render_template('login.html',res=res)	
	else:
		res={'msg':''}
		return render_template('login.html',res=res)

@app.route('/manager')
def manager():
	return render_template('manager.html')

@app.route('/selectusers')
def selectusers():
	sql = "select * from user;"
	cur.execute(sql)
	data = cur.fetchall()
	print data
	#print data
	return render_template('userlist.html',data=data)

@app.route('/userinfo')
def userinfo():
	username = request.args.get('username')
	return render_template('userinfo.html',username=username)

@app.route('/oneuser')
def oneuser():
	if request.method=='GET':
		username=request.args.get('username')
		print username
		sql = "select id,username,password,age,phone,email,role from user where username="'"%s"'";"%(username)
		cur.execute(sql)
		data = cur.fetchone()
		print data
		return render_template('oneuser.html',username=username,data=data)

@app.route('/deleteuser')	
def deleteuser():
	uid = request.args.get('id')
	print uid
	sql = 'delete from user where id=%s'%(uid)
	cur.execute(sql)
	return redirect('/selectusers')

@app.route('/updateuser',methods=['GET','POST'])
def updateuser():
	res={'msg':''}
	if request.method == 'POST':
		uid = request.args.get('id')
		password = request.form.get('password')
		repwd = request.form.get('repwd')
		print uid,password,repwd
		res = {'msg':''}
		if password == repwd:
			sql = 'update user set password="'"%s"'" where id=%s;'%(password,uid)
			print sql
			cur.execute(sql)
			res['msg']='Password update ok !'
			print res
			return render_template('update.html',res=res,uid=uid)
		else:
			res['msg']='Password not match !'
			return render_template('update.html',res=res,uid=uid)
	else:
		uid = request.args.get('id')
		print uid
		return render_template('update.html',res=res,uid=uid)
	
cur.close
conn.close

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9999, debug=True)
