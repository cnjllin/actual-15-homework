#/usr/bin/python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask,request,render_template,redirect
import MySQLdb as mysql
db=mysql.connect(host="127.0.0.1 ",user="root",passwd="ilikeit",db="reboot15",port=3306,charset
='utf8')
db.autocommit(True)
cur = db.cursor()
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/userlist/',methods=['GET','POST'])
def userlist():
    sql = 'select * from user'
    if cur.execute(sql):
        user_data=cur.fetchall()
        return render_template('userlist.html',data=user_data)

@app.route('/delete_user/')
def delete_user():
    id = request.args.get('id')
    sql = 'delete from user where id = %s' %id
    cur.execute(sql)
    return redirect('/userlist')

@app.route('/update_user/',methods=['GET','POST'])
def updateuser():
    res={'msg':''}
    if request.method == 'POST':
        uid = request.args.get('id')
        print "uid:%s" %uid
        password = request.form.get('password')
        repwd = request.form.get('repwd')
        print uid,password,repwd
        res = {'msg':''}
        if password == repwd:
            sql = "update user set password = password('%s') where id = %s" %(password,uid)
            print sql
            cur.execute(sql)
            res['msg']='密码修改成功'
            return render_template('update.html',res=res,uid=uid)
        else:
            res['msg']='密码不匹配'
            return render_template('update.html',res=res,uid=uid)
    uid = request.args.get('id')
    print uid
    return render_template('update.html',res=res,uid=uid)

@app.route('/login/',methods=["GET","POST"])
def login():
    mess = ""
    #如果前端获取的方法是POST，则接受数据
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print username,password
        #打开用户文件，将用户名存入一个列表，用户名和密码存入一个字典
        f = open('user.txt')
        l = []
        k = {}
        for i in f.readlines():
            i =i.strip('\n')
            a = i.split(':')[0]
            b = i.split(':')[1]
            k[a] = b
            l.append(a)
        #判断用户名是否存在
        if username not in l:
            #return "用户名不存在"
            mess = "用户名不存在"
        else:
            #判断密码是否正确
            if password == k.get(username):
                #return "欢迎%s登录" %username
                #mess = "欢迎%s登录" %username
                return redirect('/userlist/')
            else:
                #return "登录密码错误"
                mess = "登录密码错误"
        f.close()
    return render_template("login.html",mess=mess)


@app.route('/register/',methods=["GET","POST"])
def register():
    mess = ""
    #如果前端获取的方法是POST，则接受数据
    if request.method=='POST':
        username = request.form.get('username')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        print username,new_password,confirm_password
        m = open('user.txt','a+')
        #打开用户文件，将用户名存入一个列表，检查用户名是否被注册
        l = []
        for i in m.readlines():
            a = i.split(':')[0]
            l.append(a)
        #判断密码是否为空
        if len(username) == 0:
            #return "用户名不能为空"
            mess = "用户名不能为空"
        elif username in l:
            #return "账户已被注册"
            mess = "账户已被注册"
        #判断密码是否为空
        elif len(new_password) == 0:
            #return "密码不能为空"
            mess = "密码不能为空"
        #判断两次输入密码是否相同
        elif confirm_password == new_password:
            m.write('%s:%s\n' %(username,new_password))
            #return "注册成功，您的账号为:%s,密码为:%s,请妥善保管" %(username,new_password)
            mess = "注册成功，您的账号为:%s,密码为:%s,请妥善保管" %(username,new_password)
        else:
            #return "密码不匹配"
            mess = "密码不匹配"
        m.close()
    return render_template("register.html",mess=mess)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
