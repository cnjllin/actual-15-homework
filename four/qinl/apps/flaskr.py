#coding: utf-8
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
from apps import app
from apps.models import Users,db, Nginxlog


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/dashboard')
def dashboard():

    with open(app.config['LOG'], 'r') as f:

        '''返回IP、URL、状态'''

        ip = [(x.split(" ")[0],x.split(" ")[6],x.split(" ")[8]) for x in f]

        '''获取IP'''
        iplist = []
        for i in ip:
             iplist.append(i[0])

        '''ip 去重'''
        iplist2 = []
        for  i in iplist:
            if i in iplist2:
                continue
            else:
                iplist2.append(i)

        '''统计IP数量'''
        iplist3 = []
        for i in iplist2:
            iplist3.append((i,iplist.count(i)))

        '''排序'''
        for i in range(0, len(iplist3)):
            for j in range(i + 1, len(iplist3)):
                if iplist3[i][1] > iplist3[j][1]:
                    iplist3[i], iplist3[j] = iplist3[j], iplist3[i]

        iplist4 = iplist3[-10:]
        iplist4.reverse()

    return render_template('dashboard.html',user=iplist4)

@app.route('/login/',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Users.query.filter_by(username=request.form['username']).first()
        if user is not None and request.form['password'] == user.password:
            #login_user(user)
            #flash(u'登录成功')
            session['logged_in'] = True
            return redirect('dashboard')

        else:
            flash(u'用户或密码错误')
            print 'error'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


