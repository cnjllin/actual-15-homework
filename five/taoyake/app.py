#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask import Flask,render_template,request,redirect
import util
import MySQLdb as mysql
con = mysql.connect(host="localhost",user="root",passwd="123456",db="reboot15",port=3306,charset='utf8')
con.autocommit(True)
cur=con.cursor()

app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def index():
    welcome = 'hello world'
    return render_template('index.html',welcome=welcome)



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 验证登录用户
        sql = 'select * from taoyake where username="%s"' % (username)
        status = util.chk_login(username,password,sql)
        if status:
            return redirect('/userlist')
        else:
            return status

@app.route('/userlist')
def userlist():
    sql = 'select * from taoyake'
    res = util.select(sql)
    print res
    return render_template('userlist.html',res=res)



@app.route('/user/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        sex = request.form.get('sex')
        age = request.form.get('age')
        phone = request.form.get('phone')
        email = request.form.get('email')
        role = request.form.get('role')
        sql = 'insert into taoyake values("%s","%s","%s","%s","%s","%s","%s");' % (username,password,sex,age,phone,email,role)
        args = (username,password,sex,age,phone,email,role)
        print args

@app.route('/user/update/',methods=['GET','POST'])
def update():
    res={'msg':''} 
    if request.method == 'GET':
        uid = request.args.get('uid')
        return render_template('update.html',res=res,uid=uid)
    if request.method == 'POST':
        uid = request.form.get('uid')
        password = request.form.get('password')
        repwd = request.form.get('repwd')
        print uid,password,repwd
        res = {'msg':''}
        if password == repwd:
            sql = 'update taoyake set password="'"%s"'" where id=%s;'%(password,uid)
            print sql
            cur.execute(sql)
            res['msg']=True
            print True
            return redirect('/userlist')
            #return render_template('update.html',res=res,uid=uid)
        else:
            res['msg'] = '两次输入的密码不一致，请重新输入'
            return render_template('update.html',res=res,uid=uid)

"""删除用户信息
"""
@app.route('/user/delete/')
def DeleteUser():
    if request.method == 'GET':
        uid = int(request.args.get('uid'))
        print uid
        sql = 'delete from taoyake  where id=%d;' % (uid)
        if util.del_user(uid, sql):
            return redirect('/userlist')
        
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
