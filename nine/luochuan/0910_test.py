# -*- coding: utf-8 -*-
import MySQLdb as mysql
from flask import Flask,render_template,request,session,redirect
import json,util2,util,db_config

db=mysql.connect(db_config.host,db_config.user,db_config.passwd,db_config.db,db_config.port,db_config.charset)
db.cursor()
cur = db.cursor()
app = Flask(__name__)
app.secret_key = 'sadaredfs'
table = 'user'
field = ['id','username', 'password', 'role', 'email', 'phone']
field01 = ['username', 'password', 'role', 'email', 'phone']



@app.route('/logout/')
def logout():
    if session:
        session.clear()
        return redirect('/login/')
    else:
        return redirect('/login/')


@app.route('/')
def hello_world():
    if not session:
        return redirect('/login/')
    else:
        name = session['username']
        result = util2.getone(name)
        return render_template('hello world.html',result=result,session=session)

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = dict(request.form)
        data = {k:v[0] for k,v in data.items()}
        name = data.get('username', '')
        passwd = data.get('password', '')
        result = util2.logincheck(name,passwd)
        if result['code'] == 1:
            session['username'] = result['username']
            session['role'] = result['role']
            session['id'] = result['id']
            util.WriteLog('session result').info('session result : %s' % session)
            return json.dumps(result)
    else:
        return render_template("login.html")

@app.route('/register/',methods=['GET','POST'])
def register():
    if session:
        if request.method == 'POST':
            dict_reg = dict((k, v[0]) for k, v in dict(request.form).items())
            data = util2.useradd('user', field01, dict_reg)
            return json.dumps(data)
    else:
        return redirect('/')

@app.route('/userlist/')
def userlist():
    if session:
        userdict = util2.admlist()
        print userdict
        return render_template('userlist.html', userdict=userdict)
    return redirect('/login/')

@app.route('/update/',methods=['GET','POST'])
def update():
    if  not session:
        return redirect('/login/')
    if request.method == 'POST':
        user = {k:v[0] for k,v in dict(request.form).items()}
        data = util2.update('user',field,user)
        return json.dumps(data)



if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5001)
