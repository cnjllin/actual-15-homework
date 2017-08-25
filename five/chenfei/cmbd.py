#!/usr/bin/python
# __*__ conding: UTF-8 __*__

from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = 'adsfasfasfasdfasd567566546gdfsgsd'
import MySQLdb as mysql

con = mysql.connect(host='127.0.0.1',user='root',passwd='123456',db='re15',port=3306)
print con
con.autocommit(True)
cur = con.cursor()

@app.route('/')
def web():
    hello = "Welcome To My Home"
    return render_template("web.html",hello=hello)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='GET':
        return render_template('add.html')
    elif request.method=='POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if (not user) or (not pwd):
             return 'need uer'
        else:
             sql = 'insert into user values ("%s","%s")'%(user,pwd)
             cur.execute(sql)
             print sql
    return  redirect('/index')

@app.route('/index')
def index():
        user = request.args.get('user')
        cur.execute('select * from user')
        res = cur.fetchall()
        return render_template('index.html',user=user,info=res)

@app.route('/del')
def delete():
    user = request.args.get('user')
    sql = 'delete from user where username="%s"'%(user)
    cur.execute(sql)
    return redirect('/add')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
       return render_template('login.html')
    elif request.method=='POST':
         user = request.form.get('user')
         pwd = request.form.get('pwd')
         

         sql = 'select * from user where username="%s" and password="%s"'%(user,pwd)
         cur.execute(sql)
         if cur.fetchone():
            return redirect('/index')
         else:
            return redirect('/login')

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='GET':
        user = request.args.get('user')
        return render_template('update.html',user=user)
    elif request.method=='POST':
        user = request.form.get('user')
        oldpwd = request.form.get('oldpwd')
        newpwd = request.form.get('newpwd')
        confirmpwd = request.form.get('confirmpwd')   
        sql = 'update user set password="%s" where username ="%s"'%(newpwd,user)
        res = cur.execute(sql)
        if res:
           return redirect('/index')
        else:
           return 'is no ok'

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8082,debug=True)
