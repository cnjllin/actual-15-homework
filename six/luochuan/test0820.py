# -*- coding: utf-8 -*-
import MySQLdb as mysql
from flask import Flask,request,render_template,redirect
import utile
db=mysql.connect(host="192.168.50.160",user="root",passwd="zhaoxf513",db="reboot15",port=3306,charset='utf8')
db.cursor()
cur = db.cursor()
app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('homepage.html')

@app.route('/signup/',methods=['POST','GET'])
def registor():
    if request.method == 'GET':
         return render_template('reg_submit.html')
    else:
         reg_dict = {}
         user_info = ['username', 'password', 'age', 'phone', 'email', 'sex', 'role']
         for i in user_info:
             reg_dict[i] = request.form.get(i)
         reg_message = utile.usercheck(**reg_dict)
         print  reg_dict
         print reg_message
         if reg_message['code'] == 1:
             return render_template('reg_fail.html')
         else:
             return render_template('reg_success.html')

@app.route('/signin/',methods=['POST','GET'])
def login():
    login_message = {'code':'0','msg':''}
    if request.method == 'GET':
        return render_template('login_submit.html')
    else:
        user = request.form.get('username', '')
        passwd = request.form.get('password', '')
        login_message = utile.logincheck(user, passwd)
        user = request.form.get('username', '')
        sql_info = "select * from user where username = '%s';"%user
        cur.execute(sql_info)
        list = cur.fetchall()
        userdict = {}
        for i in list:
            # userdict['id'] = i[0]
            userdict['name'] = ''.join(map(lambda x: "%c" % ord(x), i[1]))
            # userdict['password'] = ''.join(map(lambda x: "%c" % ord(x), i[2]))
            userdict['sex'] = i[3]
            userdict['age'] = i[4]
            userdict['phone'] = i[5]
            userdict['email'] = ''.join(map(lambda x: "%c" % ord(x), i[6]))
            # userdict['role'] = i[7]
        if login_message['code'] == 1:
            return render_template('login_success.html',userdict=userdict)
        else:
            return render_template('login_fail.html',masg=login_message)




if __name__ == '__main__':
	app.run(host='0.0.0.0',port=9999, debug=True)














