#/usr/bin/python
#coding:utf-8
from flask import Flask,render_template,request,redirect
import MySQLdb as mysql
import util

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    home = 'welcome taoyake'
    return render_template('index.html',home=home)


@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data={k:'"'+v[0]+'"' for k,v in dict(request.form).items()}
        print data
        res = util.register(data)
        if res['code'] == 0:
            return redirect('/login/')
        elif res['code'] == 1:
            print res['msg']
            return render_template("register.html",res=res)
    else:
        res={'msg':''}
        return render_template("register.html",res=res)

# 登录
@app.route('/login/',methods=['POST','GET'])
def login():
        if request.method == 'POST':
                data={k:v[0] for k,v in dict(request.form).items()}
                res = util.login(data)
                if res['code'] == 0:
                        if util.role(data)[0] == 0:
                                return redirect('/adminmanager')
                        else:
                                return render_template('userinfo.html',data=data)
                else:
                        return render_template('login.html',res=res)
        else:
                res={'msg':''}
                return render_template('login.html',res=res)

# 管理员页面
@app.route('/adminmanager/')
def manager():
        return render_template('manager.html')

# 用户列表
@app.route('/userlist/')
def userlist():
        data=util.userlist()
        return render_template('userlist.html',data=data)

# 用户删除
@app.route('/deleteuser/')
def deleteuser():
        uid=request.args.get('id')
        data={'id':uid}
        print data
        util.delete(data)
        return redirect('/userlist/')

# 用户信息更新
@app.route('/update/',methods=['GET','POST'])
def update():
        if request.method=='POST':
                data = {k:v[0] for k,v in dict(request.form).items()}
                print data
                res = util.update(data)
                if res['code']==0:
                        return redirect('/userlist')
                else:
                        return render_template('update.html',res=res)
        else:
                uid=request.args.get('id')
                data={'id':uid}
                res=util.getuser(data)
                print res
                return render_template('update.html',res=res)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
